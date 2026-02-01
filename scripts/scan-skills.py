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
import logging
import sys
from pathlib import Path

# Add scripts directory to path for imports
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from fetch_skills import fetch_top_skills, save_inventory, load_inventory, VALID_SOURCES
from run_scans import scan_skills, get_unique_repos, scan_adhoc_repos
from generate_report import aggregate_results, generate_markdown_report, generate_json_summary
from pipeline_utils import LOG_FORMAT, LOG_DATE_FORMAT

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[logging.StreamHandler()],
    )


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
        "--enable-meta",
        action="store_true",
        help="Enable meta-analysis for false positive filtering (requires --use-llm)",
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

    # Configure logging based on verbosity
    setup_logging(verbose=args.verbose)

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
            logger.error("--repo-only requires at least one --repo argument")
            sys.exit(1)
        logger.info("=" * 60)
        logger.info("STEP 1: Skipped (--repo-only mode)")
        logger.info("=" * 60)
        logger.info("Will scan %d ad-hoc repo(s)", len(args.repos))
    else:
        logger.info("=" * 60)
        logger.info("STEP 1: Fetch Skills")
        logger.info("=" * 60)

        if args.skip_fetch:
            if not inventory_path.exists():
                logger.error("--skip-fetch specified but %s not found", inventory_path)
                sys.exit(1)
            skills = load_inventory(inventory_path)
            logger.info("Loaded %d skills from %s", len(skills), inventory_path)
        else:
            label = "bottom" if args.reverse else "top"
            range_desc = f"{args.offset + 1}-{args.offset + args.count}" if args.offset else f"top {args.count}"
            logger.info("Fetching %s %d skills from %s (ranks %s)...", label, args.count, args.source, range_desc)
            try:
                skills = fetch_top_skills(args.count, offset=args.offset, reverse=args.reverse, source=args.source)
                save_inventory(skills, inventory_path)
            except Exception as e:
                logger.error("Error fetching skills: %s", e)
                sys.exit(1)

        # Display skills
        label = "Bottom" if args.reverse else "Top"
        logger.info("%s %d skills from %s:", label, len(skills), args.source)
        for s in skills[:10]:
            repo_info = f" - {s['repo']}" if s.get('repo') else ""
            logger.info("  %2d. %s (%s installs)%s", s['rank'], s['name'], f"{s['installs']:,}", repo_info)
        if len(skills) > 10:
            logger.info("  ... and %d more", len(skills) - 10)

        if args.repos:
            logger.info("Plus %d ad-hoc repo(s)", len(args.repos))

    if args.list_only:
        logger.info("--list-only specified, exiting.")
        return

    # =========================================================================
    # Step 2: Clone and Scan
    # =========================================================================
    if not args.skip_scan:
        logger.info("=" * 60)
        logger.info("STEP 2: Clone Repositories & Run Scans")
        logger.info("=" * 60)

        all_results = []

        # Scan top skills (if any)
        if skills:
            # Show what will be downloaded/cloned
            github_skills = [s for s in skills if s.get("source") == "skills.sh" and s.get("repo")]
            clawhub_skills = [s for s in skills if s.get("source") == "clawhub"]

            if github_skills:
                repos = get_unique_repos(github_skills)
                logger.info("%d unique GitHub repositories to clone:", len(repos))
                for repo in list(repos.keys())[:5]:
                    logger.info("  - %s (%d skills)", repo, len(repos[repo]))
                if len(repos) > 5:
                    logger.info("  ... and %d more", len(repos) - 5)

            if clawhub_skills:
                logger.info("%d skills to download from clawhub.ai", len(clawhub_skills))

            results = scan_skills(
                skills=skills,
                skills_dir=args.skills_dir,
                output_dir=args.output,
                scanner_path=args.scanner,
                use_llm=args.use_llm,
                enable_meta=args.enable_meta,
            )
            all_results.extend(results)

        # Scan ad-hoc repos (if any)
        if args.repos:
            logger.info("Scanning %d ad-hoc repo(s):", len(args.repos))
            for repo in args.repos:
                logger.info("  - %s", repo)

            adhoc_results = scan_adhoc_repos(
                repos=args.repos,
                skills_dir=args.skills_dir,
                output_dir=args.output,
                scanner_path=args.scanner,
                use_llm=args.use_llm,
                enable_meta=args.enable_meta,
            )
            all_results.extend(adhoc_results)

        # Quick summary
        safe = sum(1 for r in all_results if r.get("is_safe") is True)
        unsafe = sum(1 for r in all_results if r.get("is_safe") is False)
        errors = sum(1 for r in all_results if r.get("is_safe") is None)
        logger.info("Scan complete: %d safe, %d with issues, %d errors", safe, unsafe, errors)

    # =========================================================================
    # Step 3: Generate Report
    # =========================================================================
    logger.info("=" * 60)
    logger.info("STEP 3: Generate Report")
    logger.info("=" * 60)

    findings = aggregate_results(args.output)

    report_name = args.report_name or "summary-report"
    report_path = args.output / f"{report_name}.md"
    json_path = args.output / f"{report_name}.json"

    generate_markdown_report(findings, report_path)
    generate_json_summary(findings, json_path)

    # =========================================================================
    # Final Summary
    # =========================================================================
    logger.info("=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    pct = findings['safe_skills'] / max(findings['total_skills'], 1) * 100
    logger.info("Skills scanned:  %d", findings['total_skills'])
    logger.info("Safe:            %d (%.0f%%)", findings['safe_skills'], pct)
    logger.info("With issues:     %d", findings['unsafe_skills'])
    logger.info("Errors:          %d", findings['error_skills'])
    logger.info("Total findings:  %d", findings['total_findings'])
    logger.info("  CRITICAL:      %d", findings['severity_counts']['CRITICAL'])
    logger.info("  HIGH:          %d", findings['severity_counts']['HIGH'])
    logger.info("  MEDIUM:        %d", findings['severity_counts']['MEDIUM'])
    logger.info("  LOW:           %d", findings['severity_counts']['LOW'])
    logger.info("Output files:")
    logger.info("  %s", report_path)
    logger.info("  %s", json_path)
    logger.info("  %s/*-scan.json", args.output)
    logger.info("  %s/*-scan.md", args.output)

    # Exit with error code if critical/high findings
    if findings['severity_counts']['CRITICAL'] > 0:
        logger.warning("Critical findings detected!")
        sys.exit(2)
    elif findings['severity_counts']['HIGH'] > 0:
        logger.warning("High severity findings detected!")
        sys.exit(1)


if __name__ == "__main__":
    main()
