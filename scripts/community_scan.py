#!/usr/bin/env python3
"""
Community scan request handler.

Bridges GitHub Actions issue context with the existing scan pipeline.
Validates input, runs the scan, and produces a markdown comment file
for posting back to the GitHub issue.
"""

import argparse
import hashlib
import json
import logging
import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from pipeline_utils import LOG_FORMAT, LOG_DATE_FORMAT
from run_skillspector import scan_one
from run_scans import (
    run_batch_scan,
    clone_repo,
    parse_repo_arg,
    repo_to_dirname,
    run_scan,
    sanitize_filename,
)

logger = logging.getLogger(__name__)

COMMENT_OUTPUT = Path("/tmp/scan-comment.md")
MAX_COMMENT_LENGTH = 60000  # GitHub comment limit is 65536
# SkillSpector runs after the Cisco batch on the kept skill directories. Above this many
# skills it is skipped so one large request cannot push the job past its 30-minute limit
# (the corpus run did about 57 scans a minute at 4 workers).
SECOND_SCANNER_MAX_SKILLS = 300
SECOND_SCANNER_WORKERS = 4
SECOND_SCANNER_POST = "https://skillscan.io/research/2026/two-scanners-one-corpus/"


def validate_repo(repo_slug: str) -> dict:
    """
    Validate that a GitHub repo exists and is public.

    Args:
        repo_slug: Repository in "owner/repo" format

    Returns:
        Repository metadata from GitHub API

    Raises:
        SystemExit: If the repo doesn't exist, is private, or API fails
    """
    url = f"https://api.github.com/repos/{repo_slug}"
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        resp = requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as e:
        logger.error("GitHub API request failed: %s", e)
        sys.exit(1)

    if resp.status_code == 404:
        logger.error("Repository %s not found or is private", repo_slug)
        _write_error_comment(repo_slug, "Repository not found or is private.")
        sys.exit(1)

    if resp.status_code != 200:
        logger.error("GitHub API returned %d for %s", resp.status_code, repo_slug)
        _write_error_comment(repo_slug, f"GitHub API error (HTTP {resp.status_code}).")
        sys.exit(1)

    data = resp.json()

    if data.get("private"):
        logger.error("Repository %s is private — cannot scan", repo_slug)
        _write_error_comment(repo_slug, "Repository is private. Only public repos can be scanned.")
        sys.exit(1)

    return data


def check_repo_size(repo_metadata: dict, max_mb: int, repo_slug: str) -> None:
    """
    Reject repositories over the size limit.

    Args:
        repo_metadata: GitHub API response for the repo
        max_mb: Maximum allowed size in megabytes
        repo_slug: For error messages

    Raises:
        SystemExit: If repo exceeds size limit
    """
    size_kb = repo_metadata.get("size", 0)
    size_mb = size_kb / 1024

    if size_mb > max_mb:
        msg = f"Repository is {size_mb:.0f} MB, exceeding the {max_mb} MB limit."
        logger.error("%s: %s", repo_slug, msg)
        _write_error_comment(repo_slug, msg)
        sys.exit(1)

    logger.info("Repo size: %.1f MB (limit: %d MB)", size_mb, max_mb)


def dedupe_identical_skill_dirs(skill_dirs: list[Path], repo_dir: Path) -> tuple[list[Path], dict[Path, Path]]:
    """Keep one of each set of byte-identical skill directories in a repo.

    Repos that ship a canonical skills/ tree plus per-plugin copies of the same
    directories (inhotel-io/govisit-toolkit, microsoft/azure-skills) would
    otherwise get one scan, one result file, and one site page per copy. The
    shallowest path is kept, ties broken alphabetically, so skills/x wins over
    plugins/p/skills/x. Two directories are identical when they have the same
    directory name and the same relative file paths with the same bytes; the
    name is part of the key so two distinct skills that happen to share files
    are both scanned, matching how the site groups copies.

    Returns the kept directories in their original order and a copy -> kept map.
    """
    def fingerprint(d: Path) -> str:
        h = hashlib.sha256(d.name.encode())
        for f in sorted(x for x in d.rglob("*") if x.is_file()):
            h.update(f.relative_to(d).as_posix().encode())
            h.update(b"\0")
            h.update(hashlib.sha256(f.read_bytes()).digest())
        return h.hexdigest()

    def rank(d: Path) -> tuple[int, str]:
        rel = d.relative_to(repo_dir)
        return (len(rel.parts), rel.as_posix())

    primary: dict[str, Path] = {}
    copies: dict[Path, Path] = {}
    for d in sorted(skill_dirs, key=rank):
        fp = fingerprint(d)
        if fp in primary:
            copies[d] = primary[fp]
        else:
            primary[fp] = d
    return [d for d in skill_dirs if d not in copies], copies


def run_community_scan(
    repo_slug: str,
    skills_dir: Path,
    output_dir: Path,
    use_llm: bool = False,
    enable_meta: bool = False,
    skipped_copies: dict[str, str] | None = None,
    kept_skills: dict[Path, str] | None = None,
) -> list[dict]:
    """
    Clone and scan all skills in a repository.

    ``skipped_copies`` and ``kept_skills``, when given, are filled with the
    byte-identical copies that were not scanned and the scanned directory -> result
    stem map, so the caller can run a second scanner over the same directories.

    Returns:
        List of scan result dicts
    """
    repo_dir = skills_dir / repo_to_dirname(repo_slug)

    if not clone_repo(repo_slug, repo_dir):
        _write_error_comment(repo_slug, "Failed to clone repository.")
        sys.exit(1)

    # Find all SKILL.md files
    skill_files = sorted(repo_dir.rglob("SKILL.md"))

    if not skill_files:
        _write_error_comment(repo_slug, "No SKILL.md files found in the repository.")
        sys.exit(1)

    logger.info("Found %d skill(s) in %s", len(skill_files), repo_slug)

    skill_dirs, copies = dedupe_identical_skill_dirs([f.parent for f in skill_files], repo_dir)
    if copies:
        logger.info("Skipping %d byte-identical copies of %d skill(s)", len(copies), len({v for v in copies.values()}))
        if skipped_copies is not None:
            skipped_copies.update({
                c.relative_to(repo_dir).as_posix(): k.relative_to(repo_dir).as_posix() for c, k in copies.items()
            })

    # Output file stem for each skill directory.
    names: dict[Path, str] = {}
    for skill_path in skill_dirs:
        rel_path = skill_path.relative_to(repo_dir)
        if rel_path == Path("."):
            skill_name = repo_to_dirname(repo_slug)
        else:
            skill_name = str(rel_path).replace("/", "-").lstrip(".")
        names[skill_path] = sanitize_filename(skill_name)
    if kept_skills is not None:
        kept_skills.update(names)

    # One scanner process for the whole repo. Per-skill processes cost ~4s of
    # startup each, which pushed a 177-skill repo past the CI time limit.
    owner = repo_slug.split("/")[0]
    origin = {"source": owner, "repo_url": f"https://github.com/{repo_slug}"}
    batch = run_batch_scan(repo_dir=repo_dir, output_dir=output_dir, names=names, origin=origin)

    results = []
    for skill_path, safe_name in names.items():
        if batch is not None and safe_name in batch:
            results.append(batch[safe_name])
            continue
        if batch is None:
            # Whole batch failed: fall back to the slower per-skill path.
            result = run_scan(
                skill_path=skill_path,
                output_dir=output_dir,
                skill_name=safe_name,
                use_llm=use_llm,
                enable_meta=enable_meta,
                origin=origin,
            )
            if result:
                results.append(result)
                continue
        results.append({
            "skill_name": safe_name,
            "is_safe": None,
            "error": "Scan failed",
            "findings_count": 0,
            "max_severity": "ERROR",
        })

    return results


def run_second_scanner(
    names: dict[Path, str],
    output_dir: Path,
    skillspector: str | None = None,
    max_skills: int = SECOND_SCANNER_MAX_SKILLS,
) -> dict:
    """Run NVIDIA SkillSpector (static, ``--no-llm``) over the kept skill directories.

    Writes ``<output_dir>/skillspector/<stem>-skillspector.json`` next to each Cisco
    result, in the same shape ``run_skillspector.py`` produces for the corpus, so
    ``compare_scanners.py`` picks the new verdicts up unchanged.

    Fails open: a missing executable, an over-budget repo, or a crash in one scan
    never fails the Cisco scan or the PR. Returns ``{"rows": {stem: slim_row},
    "note": str | None, "version": str | None}``; ``rows`` is empty when the
    scanner did not run and ``note`` says why, in a sentence fit for the comment.
    """
    exe = skillspector or shutil.which("skillspector")
    if not exe:
        logger.warning("skillspector not found on PATH; second-scanner verdicts skipped")
        return {"rows": {}, "note": "SkillSpector was not available in this run, so only Cisco verdicts are shown.", "version": None}
    if len(names) > max_skills:
        logger.warning("%d kept skills exceed the %d-skill SkillSpector budget; skipped", len(names), max_skills)
        return {"rows": {}, "note": f"SkillSpector was skipped: {len(names)} skills exceed the {max_skills}-skill budget for one request.", "version": None}

    ss_dir = output_dir / "skillspector"
    ss_dir.mkdir(parents=True, exist_ok=True)

    def one(item: tuple[Path, str]) -> tuple[str, dict]:
        skill_path, stem = item
        out_file = ss_dir / f"{stem}-skillspector.json"
        # SkillSpector writes nothing on a failed run and scan_one treats an existing
        # output file as success, so a stale report from an earlier request must go first.
        out_file.unlink(missing_ok=True)
        try:
            return stem, scan_one(exe, skill_path, out_file, output_dir / f"{stem}-scan.json")
        except Exception as e:  # noqa: BLE001 - one bad scan must not sink the batch
            return stem, {"name": out_file.stem, "error": f"{type(e).__name__}: {e}"[:500]}

    rows: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=SECOND_SCANNER_WORKERS) as pool:
        for stem, row in pool.map(one, names.items()):
            rows[stem] = row

    version = None
    for stem in rows:
        out_file = ss_dir / f"{stem}-skillspector.json"
        if "error" not in rows[stem] and out_file.exists():
            try:
                version = (json.loads(out_file.read_text()).get("metadata") or {}).get("skillspector_version")
            except (OSError, ValueError):
                version = None
            if version:
                break
    errors = sum(1 for r in rows.values() if "error" in r)
    logger.info("SkillSpector: %d scanned, %d errors (version %s)", len(rows) - errors, errors, version or "unknown")
    return {"rows": rows, "note": None, "version": version}


def _second_cell(row: dict | None) -> str:
    if row is None:
        return "—"
    if "error" in row:
        return "error"
    return f"{row.get('recommendation') or 'UNKNOWN'} {row.get('score') if row.get('score') is not None else '?'}"


def format_results_comment(
    repo_slug: str,
    results: list[dict],
    skipped_copies: dict[str, str] | None = None,
    second: dict | None = None,
) -> str:
    """
    Format scan results as a GitHub-flavored markdown comment.

    Args:
        repo_slug: The scanned repository
        results: List of scan result dicts
        skipped_copies: byte-identical directories that were not scanned -> the one that was
        second: ``run_second_scanner`` output. When present and it has rows, the per-skill
            table gains a SkillSpector column and the metrics gain two rows. Only the
            recommendation and score are rendered, never finding text, because the comment
            is public. ``None`` leaves the comment exactly as before.

    Returns:
        Markdown string for the issue comment
    """
    total = len(results)
    safe = sum(1 for r in results if r.get("is_safe") is True)
    unsafe = sum(1 for r in results if r.get("is_safe") is False)
    errors = sum(1 for r in results if r.get("is_safe") is None)

    total_findings = sum(r.get("findings_count", 0) for r in results)

    ss_rows: dict[str, dict] = (second or {}).get("rows") or {}
    # Score-0 CAUTION is SkillSpector's fail-closed "could not finish analysis" verdict,
    # which the site reports as "not fully inspected", not as a finding.
    ss_flagged = sum(1 for r in ss_rows.values() if "error" not in r and r.get("recommendation") != "SAFE" and (r.get("score") or 0) > 0)
    ss_partial = sum(1 for r in ss_rows.values() if "error" not in r and r.get("recommendation") != "SAFE" and (r.get("score") or 0) == 0)

    lines = [
        f"## Scan Results for `{repo_slug}`",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Skills Found | {total} |",
        f"| Safe | {safe} |",
        f"| Issues Found | {unsafe} |",
        f"| Errors | {errors} |",
        f"| Total Findings | {total_findings} |",
    ]
    if ss_rows:
        lines.append(f"| SkillSpector flagged | {ss_flagged} |")
        lines.append(f"| SkillSpector not fully inspected | {ss_partial} |")
    lines.append("")

    # Per-skill breakdown
    if total > 0:
        lines.append("### Per-Skill Results")
        lines.append("")
        if ss_rows:
            lines.append("| Skill | Safe | Findings | Max Severity | SkillSpector |")
            lines.append("|-------|------|----------|--------------|--------------|")
        else:
            lines.append("| Skill | Safe | Findings | Max Severity |")
            lines.append("|-------|------|----------|--------------|")

        for r in sorted(results, key=lambda x: -x.get("findings_count", 0)):
            name = r.get("skill_name", "unknown")
            is_safe = r.get("is_safe")
            if is_safe is True:
                safe_str = "Yes"
            elif is_safe is False:
                safe_str = "**No**"
            else:
                safe_str = "Error"
            count = r.get("findings_count", 0)
            severity = r.get("max_severity", "UNKNOWN")
            if ss_rows:
                lines.append(f"| {name} | {safe_str} | {count} | {severity} | {_second_cell(ss_rows.get(name))} |")
            else:
                lines.append(f"| {name} | {safe_str} | {count} | {severity} |")

        lines.append("")

    if second is not None:
        if ss_rows:
            version = second.get("version") or "2.12.0"
            lines.append(f"SkillSpector {version}, static mode (`--no-llm`); recommendation and risk score shown. "
                         f"Verdicts and the agreement with Cisco are explained in [Two scanners, one corpus]({SECOND_SCANNER_POST}).")
            lines.append("")
        if second.get("note"):
            lines.append(second["note"])
            lines.append("")

    if skipped_copies:
        kept = sorted({v for v in skipped_copies.values()})
        lines.append(f"### Skipped {len(skipped_copies)} byte-identical copies of {len(kept)} skill(s)")
        lines.append("")
        lines.append("Each copy below has the same files as the scanned directory it points to, so one scan covers it.")
        lines.append("")
        lines.append("<details><summary>Copies</summary>")
        lines.append("")
        for copy, primary in sorted(skipped_copies.items()):
            lines.append(f"- `{copy}` → `{primary}`")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Show findings detail for skills with issues
    for r in results:
        if not r.get("findings"):
            continue

        lines.append(f"### Findings: {r.get('skill_name', 'unknown')}")
        lines.append("")

        for f in r["findings"][:20]:  # Cap at 20 findings per skill
            severity = f.get("severity", "UNKNOWN")
            category = f.get("category", "unknown")
            title = f.get("title", "Untitled")
            desc = f.get("description", "")
            rule_id = f.get("rule_id", "")

            lines.append(f"**[{severity}]** {title}")
            lines.append(f"- Rule: `{rule_id}` | Category: `{category}`")
            if desc:
                # Truncate long descriptions
                if len(desc) > 300:
                    desc = desc[:297] + "..."
                lines.append(f"- {desc}")
            lines.append("")

        if len(r["findings"]) > 20:
            remaining = len(r["findings"]) - 20
            lines.append(f"*... and {remaining} more findings*")
            lines.append("")

    lines.append("---")
    lines.append("*A PR has been opened to publish these results to the [dashboard](https://skillscan.io).*")

    comment = "\n".join(lines)

    # Truncate if too long
    if len(comment) > MAX_COMMENT_LENGTH:
        truncation_notice = "\n\n*... comment truncated. See full results on the dashboard.*"
        comment = comment[: MAX_COMMENT_LENGTH - len(truncation_notice)] + truncation_notice

    return comment


def _write_error_comment(repo_slug: str, error_msg: str) -> None:
    """Write an error comment file for the workflow to post."""
    comment = (
        f"## Scan Failed for `{repo_slug}`\n\n"
        f"{error_msg}\n"
    )
    COMMENT_OUTPUT.write_text(comment)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    parser = argparse.ArgumentParser(description="Run a community-requested skill scan")
    parser.add_argument("--repo", required=True, help="GitHub repo in owner/repo format or URL")
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    parser.add_argument("--skills-dir", type=Path, default=Path("skills"))
    parser.add_argument("--max-repo-size-mb", type=int, default=500)
    parser.add_argument("--second-scanner", choices=["skillspector", "none"], default="skillspector",
                        help="Also run NVIDIA SkillSpector (static) on each kept skill directory")
    args = parser.parse_args()

    # 1. Parse and validate repo format
    try:
        repo_slug = parse_repo_arg(args.repo)
    except ValueError as e:
        logger.error("Invalid repo: %s", e)
        _write_error_comment(args.repo, f"Invalid repository format: {e}")
        sys.exit(1)

    logger.info("Processing scan request for %s", repo_slug)

    # 2. Validate repo exists and is public
    metadata = validate_repo(repo_slug)

    # 3. Check repo size
    check_repo_size(metadata, args.max_repo_size_mb, repo_slug)

    # 4. Community scans always use static analysis only.
    # LLM analysis is disabled to prevent secret exfiltration via crafted
    # SKILL.md prompt injection — a malicious skill could trick the LLM
    # into leaking the API key in scan output posted to a public issue.
    logger.info("Static analysis only (LLM disabled for community scans)")

    # 5. Run the scan
    skipped_copies: dict[str, str] = {}
    kept_skills: dict[Path, str] = {}
    results = run_community_scan(
        repo_slug=repo_slug,
        skills_dir=args.skills_dir,
        output_dir=args.output_dir,
        use_llm=False,
        enable_meta=False,
        skipped_copies=skipped_copies,
        kept_skills=kept_skills,
    )

    # 5b. Second scanner over the same directories (static only; fails open).
    second = run_second_scanner(kept_skills, args.output_dir) if args.second_scanner == "skillspector" else None

    # 6. Format and write comment
    comment = format_results_comment(repo_slug, results, skipped_copies, second)
    COMMENT_OUTPUT.write_text(comment)
    logger.info("Results written to %s", COMMENT_OUTPUT)

    # 7. Report summary
    safe = sum(1 for r in results if r.get("is_safe") is True)
    logger.info("Scan complete: %d/%d skills safe", safe, len(results))


if __name__ == "__main__":
    main()
