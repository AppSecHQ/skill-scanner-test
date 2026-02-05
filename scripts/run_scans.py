#!/usr/bin/env python3
"""
Module 2: Clone repositories and run security scans
"""

import io
import json
import logging
import re
import subprocess
import zipfile
from pathlib import Path

import requests

from pipeline_utils import get_session, shorten_path, LOG_FORMAT, LOG_DATE_FORMAT

logger = logging.getLogger(__name__)


def get_unique_repos(skills: list[dict]) -> dict[str, list[dict]]:
    """
    Group skills by repository to avoid duplicate clones.

    Returns:
        Dict mapping repo name to list of skills in that repo
    """
    repos = {}
    for skill in skills:
        repo = skill["repo"]
        if repo not in repos:
            repos[repo] = []
        repos[repo].append(skill)
    return repos


def repo_to_dirname(repo: str) -> str:
    """Convert repo name (owner/repo) to directory name."""
    return repo.replace("/", "-")


def safe_extract(zf: zipfile.ZipFile, dest: Path) -> None:
    """
    Extract ZIP file safely, preventing path traversal (Zip Slip) attacks.

    Validates that every member path resolves to a location inside the
    destination directory before extracting anything.

    Args:
        zf: An open ZipFile object
        dest: Destination directory (must already exist)

    Raises:
        ValueError: If any member would extract outside dest
    """
    dest = dest.resolve()
    for member in zf.namelist():
        member_path = (dest / member).resolve()
        if not member_path.is_relative_to(dest):
            raise ValueError(
                f"Attempted path traversal in ZIP: {member!r}"
            )
    zf.extractall(dest)


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    # Replace problematic characters with dashes
    sanitized = re.sub(r'[<>:"/\\|?*()[\]{}]', '-', name)
    # Replace spaces with dashes
    sanitized = sanitized.replace(' ', '-')
    # Replace multiple dashes with single dash
    sanitized = re.sub(r'-+', '-', sanitized)
    # Remove leading/trailing dashes and whitespace
    sanitized = sanitized.strip('- ')
    return sanitized.lower()


def clone_repo(repo: str, dest: Path, shallow: bool = True) -> bool:
    """
    Clone a repository if not already present.

    Args:
        repo: Repository in format "owner/repo"
        dest: Destination directory
        shallow: Use shallow clone (--depth=1) for speed

    Returns:
        True if successful or already exists, False on error
    """
    if dest.exists():
        logger.info("Repo %s already cloned, skipping", repo)
        return True

    url = f"https://github.com/{repo}.git"
    cmd = ["git", "clone"]
    if shallow:
        cmd.extend(["--depth=1"])
    cmd.extend([url, str(dest)])

    logger.info("Cloning %s...", repo)
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=CLONE_TIMEOUT_SECONDS
        )
    except subprocess.TimeoutExpired:
        logger.error("Clone of %s timed out after %ds", repo, CLONE_TIMEOUT_SECONDS)
        return False

    if result.returncode != 0:
        logger.error("Failed to clone %s: %s", repo, result.stderr)
        return False

    return True


def download_clawhub_skill(slug: str, dest: Path) -> bool:
    """
    Download a skill from clawhub.ai.

    Args:
        slug: Skill slug/identifier
        dest: Destination directory

    Returns:
        True if successful or already exists, False on error
    """
    if dest.exists():
        logger.info("Skill %s already downloaded, skipping", slug)
        return True

    url = f"https://auth.clawdhub.com/api/v1/download?slug={slug}"

    logger.info("Downloading %s...", slug)
    try:
        session = get_session()
        response = session.get(url, timeout=60)
        response.raise_for_status()

        # Extract ZIP to destination
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            safe_extract(zf, dest)

        return True

    except requests.RequestException as e:
        logger.error("Failed to download %s: %s", slug, e)
        return False
    except zipfile.BadZipFile as e:
        logger.error("Invalid ZIP for %s: %s", slug, e)
        return False
    except ValueError as e:
        logger.error("Unsafe ZIP for %s: %s", slug, e)
        return False


def find_skill_path(repo_dir: Path, skill_name: str) -> Path | None:
    """
    Locate the skill directory within a repository.

    Tries common patterns:
    1. repo/skills/{skill_name}/SKILL.md
    2. repo/skills/{normalized_name}/SKILL.md
    3. repo/{skill_name}/SKILL.md
    4. repo/SKILL.md (entire repo is the skill)

    Returns:
        Path to skill directory, or None if not found
    """
    # Normalize skill name (remove common prefixes)
    normalized = skill_name
    for prefix in ["vercel-", "expo-"]:
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]

    # Try various path patterns
    candidates = [
        repo_dir / "skills" / skill_name,
        repo_dir / "skills" / normalized,
        repo_dir / skill_name,
        repo_dir / normalized,
        repo_dir,  # Entire repo is the skill
    ]

    for path in candidates:
        skill_md = path / "SKILL.md"
        if skill_md.exists():
            return path

    # Fallback: search for SKILL.md anywhere
    skill_files = list(repo_dir.rglob("SKILL.md"))
    if skill_files:
        # Find the one that best matches the skill name
        for sf in skill_files:
            if skill_name in str(sf) or normalized in str(sf):
                return sf.parent

        # Return first found as last resort
        return skill_files[0].parent

    return None


CLONE_TIMEOUT_SECONDS = 120  # 2 minutes per clone
SCAN_TIMEOUT_SECONDS = 300  # 5 minutes per scan


def check_analysis_quality(
    result: dict,
    use_llm: bool,
    enable_meta: bool,
    skill_name: str,
) -> dict:
    """
    Check whether LLM and meta analysis actually succeeded after a scan.

    Returns a dict with:
        llm_ok: bool | None (None if not requested)
        meta_ok: bool | None
        warnings: list[str]
    """
    quality: dict = {"llm_ok": None, "meta_ok": None, "warnings": []}
    findings = result.get("findings", [])
    analyzers = result.get("analyzers_used", [])
    duration = result.get("scan_duration_seconds", 0)

    if enable_meta:
        if "meta_analyzer" not in analyzers:
            # Meta is legitimately skipped when there are 0 findings
            if findings:
                quality["meta_ok"] = False
                quality["warnings"].append(
                    f"{skill_name}: meta requested but not in analyzers_used"
                )
        elif findings:
            has_validated = any(
                "meta_validated" in f.get("metadata", {}) for f in findings
            )
            if not has_validated:
                quality["meta_ok"] = False
                quality["warnings"].append(
                    f"{skill_name}: meta ran but no meta_validated enrichment "
                    f"(silent failure, {duration:.1f}s)"
                )
            else:
                quality["meta_ok"] = True

    if use_llm:
        if "llm_analyzer" not in analyzers:
            quality["llm_ok"] = False
            quality["warnings"].append(
                f"{skill_name}: LLM requested but not in analyzers_used"
            )
        elif any(f.get("analyzer") == "llm" for f in findings):
            quality["llm_ok"] = True
        elif findings and duration < 1.0:
            quality["llm_ok"] = False
            quality["warnings"].append(
                f"{skill_name}: LLM produced no findings + fast scan "
                f"({duration:.1f}s, likely API failure)"
            )

    return quality


def run_scan(
    skill_path: Path,
    output_dir: Path,
    skill_name: str,
    scanner_path: str = "skill-scanner",
    use_behavioral: bool = True,
    use_trigger: bool = True,
    use_llm: bool = False,
    enable_meta: bool = False,
) -> dict | None:
    """
    Run skill-scanner on a skill directory.

    Args:
        skill_path: Path to the skill directory
        output_dir: Directory for output files
        skill_name: Name for output files
        scanner_path: Path to skill-scanner executable
        use_behavioral: Enable behavioral analyzer
        use_trigger: Enable trigger analyzer
        use_llm: Enable LLM analyzer (requires API key)

    Returns:
        Scan results dict, or None on error
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    json_output = output_dir / f"{skill_name}-scan.json"
    md_output = output_dir / f"{skill_name}-scan.md"

    # Build command
    cmd = [scanner_path, "scan", str(skill_path)]

    if use_behavioral:
        cmd.append("--use-behavioral")
    if use_trigger:
        cmd.append("--use-trigger")
    if use_llm:
        cmd.append("--use-llm")
    if enable_meta:
        cmd.append("--enable-meta")

    # Run JSON scan
    json_cmd = cmd + ["--format", "json", "-o", str(json_output)]
    try:
        result = subprocess.run(
            json_cmd, capture_output=True, text=True, timeout=SCAN_TIMEOUT_SECONDS
        )
    except subprocess.TimeoutExpired:
        logger.error("Scan timed out after %ds", SCAN_TIMEOUT_SECONDS)
        return None

    # Save scan log (scanner stdout + stderr)
    log_file = output_dir / f"{skill_name}-scan.log"
    with open(log_file, "w") as lf:
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        if isinstance(stdout, str) and stdout:
            lf.write(stdout)
        if isinstance(stderr, str) and stderr:
            lf.write(stderr)

    if result.returncode != 0:
        logger.error("Scan failed: %s", result.stderr)
        return None

    # Run Markdown scan
    md_cmd = cmd + ["--format", "markdown", "-o", str(md_output)]
    try:
        subprocess.run(
            md_cmd, capture_output=True, text=True, timeout=SCAN_TIMEOUT_SECONDS
        )
    except subprocess.TimeoutExpired:
        logger.warning("Markdown scan timed out after %ds", SCAN_TIMEOUT_SECONDS)

    # Post-process: shorten absolute paths in output files
    abs_path = str(skill_path.resolve())
    short = shorten_path(abs_path)
    if abs_path != short:
        # Fix JSON
        if json_output.exists():
            text = json_output.read_text()
            json_output.write_text(text.replace(abs_path, short))
        # Fix Markdown
        if md_output.exists():
            text = md_output.read_text()
            md_output.write_text(text.replace(abs_path, short))

    # Load and return results
    try:
        with open(json_output) as f:
            scan_result = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error("Failed to read scan results: %s", e)
        return None

    # Check analysis quality
    if use_llm or enable_meta:
        quality = check_analysis_quality(
            scan_result, use_llm, enable_meta, skill_name,
        )
        for warning in quality["warnings"]:
            logger.warning(warning)
        scan_result["_analysis_quality"] = quality

    return scan_result


def _log_quality_summary(results: list[dict], use_llm: bool, enable_meta: bool) -> None:
    """Log a summary of LLM/meta analysis quality across scan results."""
    if not use_llm and not enable_meta:
        return

    quality_results = [r for r in results if "_analysis_quality" in r]
    if not quality_results:
        return

    total = len(quality_results)
    if use_llm:
        llm_ok = sum(1 for r in quality_results if r["_analysis_quality"].get("llm_ok") is True)
        logger.info("LLM analysis: %d/%d scans produced real findings", llm_ok, total)
    if enable_meta:
        meta_ok = sum(1 for r in quality_results if r["_analysis_quality"].get("meta_ok") is True)
        logger.info("Meta analysis: %d/%d scans produced real enrichment", meta_ok, total)

    failed = sum(
        1 for r in quality_results
        if r["_analysis_quality"].get("llm_ok") is False
        or r["_analysis_quality"].get("meta_ok") is False
    )
    if failed:
        logger.warning(
            "%d/%d scans had silent analysis failures — check API key/credits",
            failed, total,
        )


def scan_skills(
    skills: list[dict],
    skills_dir: Path,
    output_dir: Path,
    scanner_path: str = "skill-scanner",
    use_llm: bool = False,
    enable_meta: bool = False,
) -> list[dict]:
    """
    Download/clone and scan all skills.

    Supports multiple sources:
    - skills.sh: Clone from GitHub repos
    - clawhub: Download ZIP files

    Args:
        skills: List of skill dictionaries (must include 'source' field)
        skills_dir: Directory for downloaded/cloned skills
        output_dir: Directory for scan results
        scanner_path: Path to skill-scanner executable
        use_llm: Enable LLM analyzer

    Returns:
        List of scan results
    """
    skills_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Separate skills by source
    github_skills = [s for s in skills if s.get("source") == "skills.sh" and s.get("repo")]
    clawhub_skills = [s for s in skills if s.get("source") == "clawhub"]

    # Clone GitHub repos (skills.sh)
    if github_skills:
        repos = get_unique_repos(github_skills)
        logger.info("Cloning %d unique GitHub repositories...", len(repos))
        for repo in repos:
            repo_dir = skills_dir / repo_to_dirname(repo)
            clone_repo(repo, repo_dir)

    # Download clawhub skills
    if clawhub_skills:
        logger.info("Downloading %d skills from clawhub...", len(clawhub_skills))
        for skill in clawhub_skills:
            skill_dir = skills_dir / f"clawhub-{skill['id']}"
            download_clawhub_skill(skill["id"], skill_dir)

    # Scan all skills
    logger.info("Scanning %d skills...", len(skills))
    results = []

    for skill in skills:
        source = skill.get("source", "skills.sh")

        # Determine skill directory based on source
        if source == "clawhub":
            skill_dir = skills_dir / f"clawhub-{skill['id']}"
            # Clawhub skills have SKILL.md at root of extracted ZIP
            skill_path = skill_dir if (skill_dir / "SKILL.md").exists() else None
        else:
            # GitHub-based (skills.sh)
            if not skill.get("repo"):
                logger.warning("[%2d] %s - skipping, no repo", skill["rank"], skill["name"])
                results.append({
                    "skill_name": skill["name"],
                    "is_safe": None,
                    "error": "No repo specified",
                    "findings_count": 0,
                    "max_severity": "UNKNOWN",
                })
                continue
            repo_dir = skills_dir / repo_to_dirname(skill["repo"])
            skill_path = find_skill_path(repo_dir, skill["name"])

        if skill_path is None:
            logger.warning("[%2d] %s - skipping, SKILL.md not found", skill["rank"], skill["name"])
            results.append({
                "skill_name": skill["name"],
                "is_safe": None,
                "error": "SKILL.md not found",
                "findings_count": 0,
                "max_severity": "UNKNOWN",
            })
            continue

        # Sanitize skill name for use in filenames
        safe_name = sanitize_filename(skill["name"])

        result = run_scan(
            skill_path=skill_path,
            output_dir=output_dir,
            skill_name=safe_name,
            scanner_path=scanner_path,
            use_llm=use_llm,
            enable_meta=enable_meta,
        )

        if result:
            status = "SAFE" if result.get("is_safe") else f"ISSUES ({result.get('findings_count', 0)})"
            logger.info("[%2d] %s - %s", skill["rank"], skill["name"], status)
            results.append(result)
        else:
            logger.error("[%2d] %s - scan failed", skill["rank"], skill["name"])
            results.append({
                "skill_name": skill["name"],
                "is_safe": None,
                "error": "Scan failed",
                "findings_count": 0,
                "max_severity": "ERROR",
            })

    _log_quality_summary(results, use_llm, enable_meta)
    return results


def parse_repo_arg(repo: str) -> str:
    """
    Parse a repo argument into owner/repo format.

    Handles:
        - owner/repo
        - https://github.com/owner/repo
        - https://github.com/owner/repo.git
        - github.com/owner/repo

    Returns:
        Repository in "owner/repo" format
    """
    repo = repo.strip()

    # Remove .git suffix
    if repo.endswith(".git"):
        repo = repo[:-4]

    # Handle full URLs
    if "github.com/" in repo:
        # Extract owner/repo from URL
        parts = repo.split("github.com/")[-1].split("/")
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"

    # Already in owner/repo format
    if "/" in repo and not repo.startswith("http"):
        return repo

    raise ValueError(f"Invalid repo format: {repo}. Expected 'owner/repo' or GitHub URL.")


def scan_adhoc_repos(
    repos: list[str],
    skills_dir: Path,
    output_dir: Path,
    scanner_path: str = "skill-scanner",
    use_llm: bool = False,
    enable_meta: bool = False,
) -> list[dict]:
    """
    Clone and scan all skills in arbitrary GitHub repositories.

    Args:
        repos: List of repos in "owner/repo" format or GitHub URLs
        skills_dir: Directory for cloned repositories
        output_dir: Directory for scan results
        scanner_path: Path to skill-scanner executable
        use_llm: Enable LLM analyzer

    Returns:
        List of scan results for each SKILL.md found
    """
    skills_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for repo_arg in repos:
        try:
            repo = parse_repo_arg(repo_arg)
        except ValueError as e:
            logger.error("Invalid repo argument: %s", e)
            continue

        repo_dir = skills_dir / repo_to_dirname(repo)

        # Clone the repo
        logger.info("Processing %s...", repo)
        if not clone_repo(repo, repo_dir):
            results.append({
                "skill_name": repo,
                "is_safe": None,
                "error": "Clone failed",
                "findings_count": 0,
                "max_severity": "ERROR",
            })
            continue

        # Find all SKILL.md files in the repo
        skill_files = list(repo_dir.rglob("SKILL.md"))

        if not skill_files:
            logger.warning("No SKILL.md files found in %s", repo)
            results.append({
                "skill_name": repo,
                "is_safe": None,
                "error": "No SKILL.md found",
                "findings_count": 0,
                "max_severity": "UNKNOWN",
            })
            continue

        logger.info("Found %d skill(s) in %s", len(skill_files), repo)

        # Scan each skill
        for skill_md in skill_files:
            skill_path = skill_md.parent

            # Derive skill name from path
            rel_path = skill_path.relative_to(repo_dir)
            if rel_path == Path("."):
                skill_name = repo_to_dirname(repo)
            else:
                skill_name = str(rel_path).replace("/", "-").lstrip(".")

            result = run_scan(
                skill_path=skill_path,
                output_dir=output_dir,
                skill_name=skill_name,
                scanner_path=scanner_path,
                use_llm=use_llm,
                enable_meta=enable_meta,
            )

            if result:
                status = "SAFE" if result.get("is_safe") else f"ISSUES ({result.get('findings_count', 0)})"
                logger.info("Scanning %s - %s", skill_name, status)
                results.append(result)
            else:
                logger.error("Scan failed for %s", skill_name)
                results.append({
                    "skill_name": skill_name,
                    "is_safe": None,
                    "error": "Scan failed",
                    "findings_count": 0,
                    "max_severity": "ERROR",
                })

    _log_quality_summary(results, use_llm, enable_meta)
    return results


if __name__ == "__main__":
    import argparse
    from fetch_skills import load_inventory

    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    parser = argparse.ArgumentParser(description="Run security scans on skills")
    parser.add_argument("-i", "--inventory", type=Path, required=True, help="Path to skill-inventory.json")
    parser.add_argument("-s", "--skills-dir", type=Path, default=Path("skills"), help="Directory for cloned repos")
    parser.add_argument("-o", "--output", type=Path, default=Path("results"), help="Output directory")
    parser.add_argument("--scanner", type=str, default="skill-scanner", help="Path to skill-scanner")
    parser.add_argument("--use-llm", action="store_true", help="Enable LLM analyzer")
    parser.add_argument("--enable-meta", action="store_true", help="Enable meta-analysis")
    args = parser.parse_args()

    skills = load_inventory(args.inventory)
    results = scan_skills(
        skills=skills,
        skills_dir=args.skills_dir,
        output_dir=args.output,
        scanner_path=args.scanner,
        use_llm=args.use_llm,
        enable_meta=args.enable_meta,
    )

    safe = sum(1 for r in results if r.get("is_safe") is True)
    logger.info("Done: %d/%d skills safe", safe, len(results))
