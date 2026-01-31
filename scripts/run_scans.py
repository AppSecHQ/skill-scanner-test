#!/usr/bin/env python3
"""
Module 2: Clone repositories and run security scans
"""

import io
import json
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Optional

import requests


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


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    import re
    # Replace problematic characters with dashes
    sanitized = re.sub(r'[<>:"/\\|?*()[\]{}]', '-', name)
    # Replace multiple dashes with single dash
    sanitized = re.sub(r'-+', '-', sanitized)
    # Remove leading/trailing dashes and whitespace
    sanitized = sanitized.strip('- ')
    # Replace spaces with dashes
    sanitized = sanitized.replace(' ', '-')
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
        print(f"  [skip] {repo} already cloned")
        return True

    url = f"https://github.com/{repo}.git"
    cmd = ["git", "clone"]
    if shallow:
        cmd.extend(["--depth=1"])
    cmd.extend([url, str(dest)])

    print(f"  [clone] {repo}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  [error] Failed to clone {repo}: {result.stderr}")
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
        print(f"  [skip] {slug} already downloaded")
        return True

    url = f"https://auth.clawdhub.com/api/v1/download?slug={slug}"

    print(f"  [download] {slug}...")
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        # Extract ZIP to destination
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            zf.extractall(dest)

        return True

    except requests.RequestException as e:
        print(f"  [error] Failed to download {slug}: {e}")
        return False
    except zipfile.BadZipFile as e:
        print(f"  [error] Invalid ZIP for {slug}: {e}")
        return False


def find_skill_path(repo_dir: Path, skill_name: str) -> Optional[Path]:
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


def run_scan(
    skill_path: Path,
    output_dir: Path,
    skill_name: str,
    scanner_path: str = "skill-scanner",
    use_behavioral: bool = True,
    use_trigger: bool = True,
    use_llm: bool = False,
) -> Optional[dict]:
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

    # Run JSON scan
    json_cmd = cmd + ["--format", "json", "-o", str(json_output)]
    result = subprocess.run(json_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"    [error] Scan failed: {result.stderr}")
        return None

    # Run Markdown scan
    md_cmd = cmd + ["--format", "markdown", "-o", str(md_output)]
    subprocess.run(md_cmd, capture_output=True, text=True)

    # Load and return results
    try:
        with open(json_output) as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"    [error] Failed to read results: {e}")
        return None


def scan_skills(
    skills: list[dict],
    skills_dir: Path,
    output_dir: Path,
    scanner_path: str = "skill-scanner",
    use_llm: bool = False,
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
        print(f"\nCloning {len(repos)} unique GitHub repositories...")
        for repo in repos:
            repo_dir = skills_dir / repo_to_dirname(repo)
            clone_repo(repo, repo_dir)

    # Download clawhub skills
    if clawhub_skills:
        print(f"\nDownloading {len(clawhub_skills)} skills from clawhub...")
        for skill in clawhub_skills:
            skill_dir = skills_dir / f"clawhub-{skill['id']}"
            download_clawhub_skill(skill["id"], skill_dir)

    # Scan all skills
    print(f"\nScanning {len(skills)} skills...")
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
                print(f"  [{skill['rank']:2}] {skill['name']} - [skip] No repo")
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
            print(f"  [{skill['rank']:2}] {skill['name']} - [skip] SKILL.md not found")
            results.append({
                "skill_name": skill["name"],
                "is_safe": None,
                "error": "SKILL.md not found",
                "findings_count": 0,
                "max_severity": "UNKNOWN",
            })
            continue

        print(f"  [{skill['rank']:2}] {skill['name']}...", end=" ", flush=True)

        # Sanitize skill name for use in filenames
        safe_name = sanitize_filename(skill["name"])

        result = run_scan(
            skill_path=skill_path,
            output_dir=output_dir,
            skill_name=safe_name,
            scanner_path=scanner_path,
            use_llm=use_llm,
        )

        if result:
            status = "SAFE" if result.get("is_safe") else f"ISSUES ({result.get('findings_count', 0)})"
            print(status)
            results.append(result)
        else:
            print("[error]")
            results.append({
                "skill_name": skill["name"],
                "is_safe": None,
                "error": "Scan failed",
                "findings_count": 0,
                "max_severity": "ERROR",
            })

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
            print(f"  [error] {e}")
            continue

        repo_dir = skills_dir / repo_to_dirname(repo)

        # Clone the repo
        print(f"\nProcessing {repo}...")
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
            print(f"  [warning] No SKILL.md files found in {repo}")
            results.append({
                "skill_name": repo,
                "is_safe": None,
                "error": "No SKILL.md found",
                "findings_count": 0,
                "max_severity": "UNKNOWN",
            })
            continue

        print(f"  Found {len(skill_files)} skill(s) in {repo}")

        # Scan each skill
        for skill_md in skill_files:
            skill_path = skill_md.parent

            # Derive skill name from path
            rel_path = skill_path.relative_to(repo_dir)
            if rel_path == Path("."):
                skill_name = repo_to_dirname(repo)
            else:
                skill_name = str(rel_path).replace("/", "-")

            print(f"    Scanning {skill_name}...", end=" ", flush=True)

            result = run_scan(
                skill_path=skill_path,
                output_dir=output_dir,
                skill_name=skill_name,
                scanner_path=scanner_path,
                use_llm=use_llm,
            )

            if result:
                status = "SAFE" if result.get("is_safe") else f"ISSUES ({result.get('findings_count', 0)})"
                print(status)
                results.append(result)
            else:
                print("[error]")
                results.append({
                    "skill_name": skill_name,
                    "is_safe": None,
                    "error": "Scan failed",
                    "findings_count": 0,
                    "max_severity": "ERROR",
                })

    return results


if __name__ == "__main__":
    import argparse
    from fetch_skills import load_inventory

    parser = argparse.ArgumentParser(description="Run security scans on skills")
    parser.add_argument("-i", "--inventory", type=Path, required=True, help="Path to skill-inventory.json")
    parser.add_argument("-s", "--skills-dir", type=Path, default=Path("skills"), help="Directory for cloned repos")
    parser.add_argument("-o", "--output", type=Path, default=Path("results"), help="Output directory")
    parser.add_argument("--scanner", type=str, default="skill-scanner", help="Path to skill-scanner")
    parser.add_argument("--use-llm", action="store_true", help="Enable LLM analyzer")
    args = parser.parse_args()

    skills = load_inventory(args.inventory)
    results = scan_skills(
        skills=skills,
        skills_dir=args.skills_dir,
        output_dir=args.output,
        scanner_path=args.scanner,
        use_llm=args.use_llm,
    )

    safe = sum(1 for r in results if r.get("is_safe") is True)
    print(f"\nDone: {safe}/{len(results)} skills safe")
