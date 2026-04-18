#!/usr/bin/env python3
"""
Community scan request handler.

Bridges GitHub Actions issue context with the existing scan pipeline.
Validates input, runs the scan, and produces a markdown comment file
for posting back to the GitHub issue.
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

import requests

from pipeline_utils import LOG_FORMAT, LOG_DATE_FORMAT
from run_scans import (
    clone_repo,
    parse_repo_arg,
    repo_to_dirname,
    run_scan,
    sanitize_filename,
)

logger = logging.getLogger(__name__)

COMMENT_OUTPUT = Path("/tmp/scan-comment.md")
MAX_COMMENT_LENGTH = 60000  # GitHub comment limit is 65536


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


def run_community_scan(
    repo_slug: str,
    skills_dir: Path,
    output_dir: Path,
    use_llm: bool = False,
    enable_meta: bool = False,
) -> list[dict]:
    """
    Clone and scan all skills in a repository.

    Returns:
        List of scan result dicts
    """
    repo_dir = skills_dir / repo_to_dirname(repo_slug)

    if not clone_repo(repo_slug, repo_dir):
        _write_error_comment(repo_slug, "Failed to clone repository.")
        sys.exit(1)

    # Find all SKILL.md files
    skill_files = list(repo_dir.rglob("SKILL.md"))

    if not skill_files:
        _write_error_comment(repo_slug, "No SKILL.md files found in the repository.")
        sys.exit(1)

    logger.info("Found %d skill(s) in %s", len(skill_files), repo_slug)

    results = []
    for skill_md in skill_files:
        skill_path = skill_md.parent
        rel_path = skill_path.relative_to(repo_dir)

        if rel_path == Path("."):
            skill_name = repo_to_dirname(repo_slug)
        else:
            skill_name = str(rel_path).replace("/", "-").lstrip(".")

        safe_name = sanitize_filename(skill_name)

        result = run_scan(
            skill_path=skill_path,
            output_dir=output_dir,
            skill_name=safe_name,
            use_llm=use_llm,
            enable_meta=enable_meta,
        )

        if result:
            results.append(result)
        else:
            results.append({
                "skill_name": safe_name,
                "is_safe": None,
                "error": "Scan failed",
                "findings_count": 0,
                "max_severity": "ERROR",
            })

    return results


def format_results_comment(repo_slug: str, results: list[dict]) -> str:
    """
    Format scan results as a GitHub-flavored markdown comment.

    Args:
        repo_slug: The scanned repository
        results: List of scan result dicts

    Returns:
        Markdown string for the issue comment
    """
    total = len(results)
    safe = sum(1 for r in results if r.get("is_safe") is True)
    unsafe = sum(1 for r in results if r.get("is_safe") is False)
    errors = sum(1 for r in results if r.get("is_safe") is None)

    total_findings = sum(r.get("findings_count", 0) for r in results)

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
        "",
    ]

    # Per-skill breakdown
    if total > 0:
        lines.append("### Per-Skill Results")
        lines.append("")
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
            lines.append(f"| {name} | {safe_str} | {count} | {severity} |")

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
    results = run_community_scan(
        repo_slug=repo_slug,
        skills_dir=args.skills_dir,
        output_dir=args.output_dir,
        use_llm=False,
        enable_meta=False,
    )

    # 6. Format and write comment
    comment = format_results_comment(repo_slug, results)
    COMMENT_OUTPUT.write_text(comment)
    logger.info("Results written to %s", COMMENT_OUTPUT)

    # 7. Report summary
    safe = sum(1 for r in results if r.get("is_safe") is True)
    logger.info("Scan complete: %d/%d skills safe", safe, len(results))


if __name__ == "__main__":
    main()
