#!/usr/bin/env python3
"""
Module 3: Aggregate scan results and generate summary report
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from pipeline_utils import LOG_FORMAT, LOG_DATE_FORMAT, shorten_path

logger = logging.getLogger(__name__)

# Skills whose findings are known false positives, with explanations.
# These are rendered in a dedicated section of the summary report.
KNOWN_FALSE_POSITIVES: dict[str, str] = {
    "clawdefender": (
        "Security defense tool whose detection signatures (prompt injection patterns, "
        "dangerous command strings, ANSI codes) trigger the same rules they are designed "
        "to detect. All 37 findings are pattern arrays and documentation examples, not "
        "malicious code."
    ),
}


def aggregate_results(results_dir: Path, skills_dir: Path | None = None) -> dict:
    """
    Aggregate all scan results from JSON files.

    Args:
        results_dir: Directory containing *-scan.json files

    Returns:
        Aggregated findings dictionary
    """
    findings = {
        "scan_date": datetime.now().isoformat(),
        "total_skills": 0,
        "safe_skills": 0,
        "unsafe_skills": 0,
        "error_skills": 0,
        "severity_counts": {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0},
        "total_findings": 0,
        "skills": [],
        "findings_by_category": {},
        "top_risks": [],
    }

    # Build source lookup from inventory files
    if skills_dir is None:
        skills_dir = results_dir.parent / "skills"
    source_lookup = _build_source_lookup(skills_dir)

    # Process each scan result
    for json_file in sorted(results_dir.glob("*-scan.json")):
        try:
            with open(json_file) as f:
                result = json.load(f)
        except json.JSONDecodeError as e:
            logger.warning("Skipping corrupted file %s: %s", json_file, e)
            findings["error_skills"] += 1
            continue
        except FileNotFoundError:
            logger.warning("File not found: %s", json_file)
            findings["error_skills"] += 1
            continue

        findings["total_skills"] += 1

        is_safe = result.get("is_safe")
        if is_safe is True:
            findings["safe_skills"] += 1
        elif is_safe is False:
            findings["unsafe_skills"] += 1
        else:
            findings["error_skills"] += 1

        # Count findings by severity
        skill_findings = result.get("findings", [])
        findings["total_findings"] += len(skill_findings)

        for finding in skill_findings:
            severity = finding.get("severity", "LOW").upper()
            if severity in findings["severity_counts"]:
                findings["severity_counts"][severity] += 1

            # Track by category
            category = finding.get("category", "unknown")
            if category not in findings["findings_by_category"]:
                findings["findings_by_category"][category] = 0
            findings["findings_by_category"][category] += 1

            # Collect high/critical for top risks
            if severity in ("CRITICAL", "HIGH"):
                findings["top_risks"].append({
                    "skill": result.get("skill_name"),
                    "severity": severity,
                    "category": category,
                    "rule_id": finding.get("rule_id"),
                    "description": finding.get("description"),
                    "location": finding.get("location"),
                })

        # Add skill summary
        raw_path = result.get("skill_path") or ""
        short_path = shorten_path(raw_path) if raw_path else ""
        source = _detect_source(short_path, result.get("skill_name", ""), source_lookup)
        scan_md = json_file.with_suffix("").name + ".md"  # e.g. "clickup-skill-scan.md"
        findings["skills"].append({
            "name": result.get("skill_name"),
            "path": short_path or None,
            "source": source,
            "scan_file": scan_md,
            "is_safe": is_safe,
            "findings_count": result.get("findings_count", 0),
            "max_severity": result.get("max_severity", "SAFE"),
            "analyzers": result.get("analyzers_used", []),
        })

    # Sort skills by findings count (most findings first)
    findings["skills"].sort(key=lambda x: (-x["findings_count"], x["name"]))

    # Collect all unique analyzers used across all skills
    all_analyzers = set()
    for skill in findings["skills"]:
        all_analyzers.update(skill.get("analyzers", []))
    findings["analyzers_used"] = sorted(all_analyzers)

    return findings


def generate_markdown_report(findings: dict, output_path: Path) -> None:
    """
    Generate a Markdown summary report.

    Args:
        findings: Aggregated findings dictionary
        output_path: Path to write the report
    """
    analyzers_list = ", ".join(
        a.replace("_analyzer", "") for a in findings.get("analyzers_used", [])
    ) or "static"
    report = f"""# AI Agent Skills Security Scan Report

**Generated:** {findings['scan_date']}
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** {analyzers_list}

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | {findings['total_skills']} |
| Safe Skills | {findings['safe_skills']} ({_pct(findings['safe_skills'], findings['total_skills'])}) |
| Skills with Issues | {findings['unsafe_skills']} ({_pct(findings['unsafe_skills'], findings['total_skills'])}) |
| Scan Errors | {findings['error_skills']} |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | {findings['severity_counts']['CRITICAL']} |
| HIGH | {findings['severity_counts']['HIGH']} |
| MEDIUM | {findings['severity_counts']['MEDIUM']} |
| LOW | {findings['severity_counts']['LOW']} |
| **Total Findings** | **{findings['total_findings']}** |

"""

    # Findings by category
    if findings["findings_by_category"]:
        report += """### Findings by Category

| Category | Count |
|----------|-------|
"""
        for category, count in sorted(findings["findings_by_category"].items(), key=lambda x: -x[1]):
            report += f"| {category} | {count} |\n"
        report += "\n"

    # Results table
    report += """---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
"""
    for i, skill in enumerate(findings["skills"], 1):
        safe = "Yes" if skill["is_safe"] else ("**No**" if skill["is_safe"] is False else "Error")
        severity = skill["max_severity"]
        if severity in ("CRITICAL", "HIGH"):
            severity = f"**{severity}**"
        scan_link = quote(skill["scan_file"], safe="")
        name_col = f"[{skill['name']}]({scan_link})"
        report += f"| {i} | {name_col} | {skill['source']} | {safe} | {skill['findings_count']} | {severity} |\n"

    # Top risks
    if findings["top_risks"]:
        report += """
---

## Top Risks (Critical/High Severity)

"""
        for i, risk in enumerate(findings["top_risks"][:10], 1):
            report += f"""### {i}. [{risk['severity']}] {risk['skill']} - {risk['category']}

**Rule:** {risk['rule_id']}
**Location:** {risk.get('location', 'N/A')}

{risk['description']}

"""

    # Known false positives
    fp_skills = [s for s in findings["skills"] if s["name"] in KNOWN_FALSE_POSITIVES]
    if fp_skills:
        report += """---

## Known False Positives

The following skills were flagged by the scanner but have been manually reviewed and determined to be false positives.

| Skill | Findings | Reason |
|-------|----------|--------|
"""
        for skill in fp_skills:
            reason = KNOWN_FALSE_POSITIVES[skill["name"]]
            scan_link = quote(skill["scan_file"], safe="")
            report += f"| [{skill['name']}]({scan_link}) | {skill['findings_count']} | {reason} |\n"
        report += "\n"

    # Clean skills
    clean_skills = [s for s in findings["skills"] if s["is_safe"] is True and s["findings_count"] == 0]
    if clean_skills:
        report += """---

## Clean Skills (No Findings)

"""
        for skill in clean_skills:
            report += f"- {skill['name']}\n"

    # Footer
    analyzers_full = ", ".join(findings.get("analyzers_used", []))
    report += f"""
---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** {analyzers_full}
- **Scan Date:** {findings['scan_date']}

### Limitations

"""
    used = set(findings.get("analyzers_used", []))
    if "llm_analyzer" not in used:
        report += "- LLM-based semantic analysis not used (requires API key)\n"
    if "meta_analyzer" not in used:
        report += "- Meta-analysis for false positive filtering not used\n"
    report += "- VirusTotal binary scanning not used (requires API key)\n"
    report += "- No runtime verification - static and semantic analysis only\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report)

    logger.info("Report saved to %s", output_path)


def _pct(num: int, total: int) -> str:
    """Calculate percentage string."""
    if total == 0:
        return "0%"
    return f"{num / total * 100:.0f}%"


def _build_source_lookup(skills_dir: Path) -> dict[str, str]:
    """Build a skill_name -> source mapping from all inventory files."""
    lookup = {}
    for inv_file in skills_dir.glob("skill-inventory-*.json"):
        try:
            with open(inv_file) as f:
                skills = json.load(f)
            for skill in skills:
                name = skill.get("name", "").lower().replace(" ", "-")
                source = skill.get("source", "")
                if name and source:
                    lookup[name] = source
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return lookup


def _detect_source(skill_path: str, skill_name: str = "",
                   source_lookup: dict[str, str] | None = None) -> str:
    """Detect skill source from inventory lookup, then path heuristics."""
    # Check inventory first
    if source_lookup:
        normalized = skill_name.lower().replace(" ", "-")
        if normalized in source_lookup:
            src = source_lookup[normalized]
            # Normalize clawhub variants
            if src == "clawhub":
                return "clawhub.ai"
            return src

    # Path heuristics for skills not in any inventory
    if "clawhub-" in skill_path:
        return "clawhub.ai"

    # Split path into components: ./skills/<clone-dir>/[sub/path]
    parts = skill_path.replace("\\", "/").strip("/").split("/")
    try:
        idx = parts.index("skills")
    except ValueError:
        return "other"

    remaining = parts[idx + 1:]  # everything after "skills/"
    if len(remaining) >= 2:
        # Clone dir + sub-path -> GitHub repo
        # Not in inventory, so this is an ad-hoc repo scan
        # Derive source from clone dir owner (e.g., "anthropics-skills" -> "anthropic")
        clone_dir = remaining[0]
        owner = clone_dir.split("-")[0]
        # Strip trailing 's' for nicer display (anthropics -> anthropic)
        if owner.endswith("s") and len(owner) > 3:
            owner = owner[:-1]
        return owner

    return "other"


BEGIN_MARKER = "<!-- BEGIN SCAN RESULTS -->"
END_MARKER = "<!-- END SCAN RESULTS -->"


def update_readme(findings: dict, readme_path: Path) -> bool:
    """
    Update the Scan Results section of README.md between marker comments.

    Returns True if the README was updated, False if markers not found or file missing.
    """
    if not readme_path.exists():
        logger.warning("README not found at %s, skipping update", readme_path)
        return False

    text = readme_path.read_text()
    begin = text.find(BEGIN_MARKER)
    end = text.find(END_MARKER)
    if begin == -1 or end == -1:
        logger.warning("Scan results markers not found in %s, skipping update", readme_path)
        return False

    sc = findings["severity_counts"]
    cats = findings["findings_by_category"]

    section = f"""{BEGIN_MARKER}
## Scan Results

| Metric | Count |
|--------|-------|
| Total Skills Scanned | {findings['total_skills']} |
| Safe Skills | {findings['safe_skills']} ({_pct(findings['safe_skills'], findings['total_skills'])}) |
| Skills with Issues | {findings['unsafe_skills']} ({_pct(findings['unsafe_skills'], findings['total_skills'])}) |
| Total Findings | {findings['total_findings']} |

| Severity | Count |
|----------|-------|
| CRITICAL | {sc['CRITICAL']} |
| HIGH | {sc['HIGH']} |
| MEDIUM | {sc['MEDIUM']} |
| LOW | {sc['LOW']} |

| Category | Count |
|----------|-------|
"""
    for category, count in sorted(cats.items(), key=lambda x: -x[1]):
        section += f"| {category} | {count} |\n"

    section += f"""
- See [summary-report.md](results/summary-report.md) for detailed findings by skill, severity breakdowns, and top risks. Per-skill scan results (JSON + Markdown) are in the [`results/`](results/) directory.
{END_MARKER}"""

    updated = text[:begin] + section + text[end + len(END_MARKER):]
    readme_path.write_text(updated)
    logger.info("README updated at %s", readme_path)
    return True


def generate_json_summary(findings: dict, output_path: Path) -> None:
    """Save aggregated findings as JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(findings, f, indent=2)
    logger.info("JSON summary saved to %s", output_path)


if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    parser = argparse.ArgumentParser(description="Generate summary report from scan results")
    parser.add_argument("-i", "--input", type=Path, required=True, help="Directory with *-scan.json files")
    parser.add_argument("-o", "--output", type=Path, default=Path("results/summary-report.md"))
    parser.add_argument("--json", type=Path, help="Also output JSON summary")
    args = parser.parse_args()

    findings = aggregate_results(args.input)
    generate_markdown_report(findings, args.output)

    if args.json:
        generate_json_summary(findings, args.json)

    logger.info("Summary: %d/%d skills safe", findings['safe_skills'], findings['total_skills'])
    logger.info("Total findings: %d", findings['total_findings'])
