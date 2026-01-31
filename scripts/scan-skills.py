#!/usr/bin/env python3
"""
Skill Scanner Pipeline - Main Orchestrator

Automated security scanning of AI agent skills from multiple registries.

Usage:
    python scan-skills.py -n 25                    # Scan top 25 from skills.sh
    python scan-skills.py -n 25 --source clawhub   # Scan top 25 from clawhub.ai
    python scan-skills.py -n 15 --offset 10        # Scan skills 11-25
    python scan-skills.py -n 100 --reverse         # Scan bottom 100 skills
    python scan-skills.py --repo owner/repo --repo-only  # Scan specific repo
"""

import argparse
import sys
from pathlib import Path

# Add scripts directory to path for imports
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from fetch_skills import fetch_top_skills, save_inventory, load_inventory, VALID_SOURCES
from run_scans import scan_skills, get_unique_repos, scan_adhoc_repos
from generate_report import aggregate_results, generate_markdown_report, generate_json_summary


def main():
    parser = argparse.ArgumentParser(
        description="Scan AI agent skills from multiple registries for security issues",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -n 25                              Scan top 25 from skills.sh
  %(prog)s -n 25 --source clawhub             Scan top 25 from clawhub.ai
  %(prog)s -n 15 --offset 10                  Scan skills 11-25
  %(prog)s -n 100 --reverse                   Scan bottom 100 skills
  %(prog)s --repo owner/repo --repo-only      Scan a specific GitHub repo
  %(prog)s -n 10 --repo owner/repo            Top 10 + additional repo
  %(prog)s --report-name top-10               Custom report name
  %(prog)s --list-only                        Just list skills, don't scan
        """,
    )

    parser.add_argument(
        "-n", "--count",
        type=int,
        default=25,
        help="Number of top skills to scan (default: 25)",
    )
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Skip first N skills (e.g., --offset 10 -n 15 scans skills 11-25)",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Fetch lowest-installed skills instead of top",
    )
    parser.add_argument(
        "--source",
        choices=VALID_SOURCES,
        default="skills.sh",
        help="Registry to fetch from (default: skills.sh)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("results"),
        help="Output directory for scan results (default: results)",
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path("skills"),
        help="Directory for cloned repositories (default: skills)",
    )
    parser.add_argument(
        "--report-name",
        type=str,
        default=None,
        help="Custom name for summary report (default: summary-report)",
    )
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip fetching skills from API (use existing inventory)",
    )
    parser.add_argument(
        "--skip-clone",
        action="store_true",
        help="Skip cloning repositories (assume already cloned)",
    )
    parser.add_argument(
        "--skip-scan",
        action="store_true",
        help="Skip scanning (just generate report from existing results)",
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Enable LLM analyzer (requires SKILL_SCANNER_LLM_API_KEY)",
    )
    parser.add_argument(
        "--scanner",
        type=str,
        default=None,
        help="Path to skill-scanner executable (auto-detected if not specified)",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Only fetch and list skills, don't scan",
    )
    parser.add_argument(
        "--repo",
        action="append",
        dest="repos",
        metavar="REPO",
        help="Ad-hoc repo to scan (owner/repo or GitHub URL). Can be repeated.",
    )
    parser.add_argument(
        "--repo-only",
        action="store_true",
        help="Only scan --repo arguments, skip fetching top skills",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    # Setup directories
    args.output.mkdir(parents=True, exist_ok=True)
    args.skills_dir.mkdir(parents=True, exist_ok=True)

    inventory_path = args.skills_dir / "skill-inventory.json"

    # Auto-detect scanner path
    if args.scanner is None:
        # Try common locations
        candidates = [
            Path("/workspace/.venv/bin/skill-scanner"),
            Path.home() / ".local/bin/skill-scanner",
            Path("skill-scanner"),  # In PATH
        ]
        for candidate in candidates:
            if candidate.exists() or candidate.name == "skill-scanner":
                args.scanner = str(candidate)
                break
        else:
            args.scanner = "skill-scanner"  # Assume in PATH

    # =========================================================================
    # Step 1: Fetch skills (skip if --repo-only)
    # =========================================================================
    skills = []

    if args.repo_only:
        if not args.repos:
            print("Error: --repo-only requires at least one --repo argument")
            sys.exit(1)
        print("=" * 60)
        print("STEP 1: Skipped (--repo-only mode)")
        print("=" * 60)
        print(f"Will scan {len(args.repos)} ad-hoc repo(s)")
    else:
        print("=" * 60)
        print("STEP 1: Fetch Skills")
        print("=" * 60)

        if args.skip_fetch:
            if not inventory_path.exists():
                print(f"Error: --skip-fetch specified but {inventory_path} not found")
                sys.exit(1)
            skills = load_inventory(inventory_path)
            print(f"Loaded {len(skills)} skills from {inventory_path}")
        else:
            label = "bottom" if args.reverse else "top"
            range_desc = f"{args.offset + 1}-{args.offset + args.count}" if args.offset else f"top {args.count}"
            print(f"Fetching {label} {args.count} skills from {args.source} (ranks {range_desc})...")
            try:
                skills = fetch_top_skills(args.count, offset=args.offset, reverse=args.reverse, source=args.source)
                save_inventory(skills, inventory_path)
            except Exception as e:
                print(f"Error fetching skills: {e}")
                sys.exit(1)

        # Display skills
        label = "Bottom" if args.reverse else "Top"
        print(f"\n{label} {len(skills)} skills from {args.source}:")
        for s in skills[:10]:
            repo_info = f" - {s['repo']}" if s.get('repo') else ""
            print(f"  {s['rank']:2}. {s['name']} ({s['installs']:,} installs){repo_info}")
        if len(skills) > 10:
            print(f"  ... and {len(skills) - 10} more")

        if args.repos:
            print(f"\nPlus {len(args.repos)} ad-hoc repo(s)")

    if args.list_only:
        print("\n--list-only specified, exiting.")
        return

    # =========================================================================
    # Step 2: Clone and Scan
    # =========================================================================
    if not args.skip_scan:
        print("\n" + "=" * 60)
        print("STEP 2: Clone Repositories & Run Scans")
        print("=" * 60)

        all_results = []

        # Scan top skills (if any)
        if skills:
            # Show what will be downloaded/cloned
            github_skills = [s for s in skills if s.get("source") == "skills.sh" and s.get("repo")]
            clawhub_skills = [s for s in skills if s.get("source") == "clawhub"]

            if github_skills:
                repos = get_unique_repos(github_skills)
                print(f"\n{len(repos)} unique GitHub repositories to clone:")
                for repo in list(repos.keys())[:5]:
                    print(f"  - {repo} ({len(repos[repo])} skills)")
                if len(repos) > 5:
                    print(f"  ... and {len(repos) - 5} more")

            if clawhub_skills:
                print(f"\n{len(clawhub_skills)} skills to download from clawhub.ai")

            results = scan_skills(
                skills=skills,
                skills_dir=args.skills_dir,
                output_dir=args.output,
                scanner_path=args.scanner,
                use_llm=args.use_llm,
            )
            all_results.extend(results)

        # Scan ad-hoc repos (if any)
        if args.repos:
            print(f"\nScanning {len(args.repos)} ad-hoc repo(s):")
            for repo in args.repos:
                print(f"  - {repo}")

            adhoc_results = scan_adhoc_repos(
                repos=args.repos,
                skills_dir=args.skills_dir,
                output_dir=args.output,
                scanner_path=args.scanner,
                use_llm=args.use_llm,
            )
            all_results.extend(adhoc_results)

        # Quick summary
        safe = sum(1 for r in all_results if r.get("is_safe") is True)
        unsafe = sum(1 for r in all_results if r.get("is_safe") is False)
        errors = sum(1 for r in all_results if r.get("is_safe") is None)
        print(f"\nScan complete: {safe} safe, {unsafe} with issues, {errors} errors")

    # =========================================================================
    # Step 3: Generate Report
    # =========================================================================
    print("\n" + "=" * 60)
    print("STEP 3: Generate Report")
    print("=" * 60)

    findings = aggregate_results(args.output)

    report_name = args.report_name or "summary-report"
    report_path = args.output / f"{report_name}.md"
    json_path = args.output / f"{report_name}.json"

    generate_markdown_report(findings, report_path)
    generate_json_summary(findings, json_path)

    # =========================================================================
    # Final Summary
    # =========================================================================
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"""
Skills scanned:  {findings['total_skills']}
Safe:            {findings['safe_skills']} ({findings['safe_skills']/max(findings['total_skills'],1)*100:.0f}%)
With issues:     {findings['unsafe_skills']}
Errors:          {findings['error_skills']}

Total findings:  {findings['total_findings']}
  CRITICAL:      {findings['severity_counts']['CRITICAL']}
  HIGH:          {findings['severity_counts']['HIGH']}
  MEDIUM:        {findings['severity_counts']['MEDIUM']}
  LOW:           {findings['severity_counts']['LOW']}

Output files:
  {report_path}
  {json_path}
  {args.output}/*-scan.json
  {args.output}/*-scan.md
""")

    # Exit with error code if critical/high findings
    if findings['severity_counts']['CRITICAL'] > 0:
        print("WARNING: Critical findings detected!")
        sys.exit(2)
    elif findings['severity_counts']['HIGH'] > 0:
        print("WARNING: High severity findings detected!")
        sys.exit(1)


if __name__ == "__main__":
    main()
