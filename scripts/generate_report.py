#!/usr/bin/env python3
"""
Module 3: Aggregate scan results and generate summary report
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


def aggregate_results(results_dir: Path) -> dict:
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

    # Process each scan result
    for json_file in sorted(results_dir.glob("*-scan.json")):
        try:
            with open(json_file) as f:
                result = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
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
        findings["skills"].append({
            "name": result.get("skill_name"),
            "path": result.get("skill_path"),
            "is_safe": is_safe,
            "findings_count": result.get("findings_count", 0),
            "max_severity": result.get("max_severity", "SAFE"),
            "analyzers": result.get("analyzers_used", []),
        })

    # Sort skills by findings count (most findings first)
    findings["skills"].sort(key=lambda x: (-x["findings_count"], x["name"]))

    return findings


def generate_markdown_report(findings: dict, output_path: Path) -> None:
    """
    Generate a Markdown summary report.

    Args:
        findings: Aggregated findings dictionary
        output_path: Path to write the report
    """
    report = f"""# AI Agent Skills Security Scan Report

**Generated:** {findings['scan_date']}
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** static, behavioral, trigger

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

| # | Skill | Safe | Findings | Max Severity |
|---|-------|------|----------|--------------|
"""
    for i, skill in enumerate(findings["skills"], 1):
        safe = "Yes" if skill["is_safe"] else ("**No**" if skill["is_safe"] is False else "Error")
        severity = skill["max_severity"]
        if severity in ("CRITICAL", "HIGH"):
            severity = f"**{severity}**"
        report += f"| {i} | {skill['name']} | {safe} | {skill['findings_count']} | {severity} |\n"

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

    # Clean skills
    clean_skills = [s for s in findings["skills"] if s["is_safe"] is True and s["findings_count"] == 0]
    if clean_skills:
        report += """---

## Clean Skills (No Findings)

"""
        for skill in clean_skills:
            report += f"- {skill['name']}\n"

    # Footer
    report += f"""
---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** static_analyzer, behavioral_analyzer, trigger_analyzer
- **Scan Date:** {findings['scan_date']}

### Limitations

- LLM-based semantic analysis not used (requires API key)
- VirusTotal binary scanning not used (requires API key)
- Static analysis only - no runtime verification
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report)

    print(f"Report saved to {output_path}")


def _pct(num: int, total: int) -> str:
    """Calculate percentage string."""
    if total == 0:
        return "0%"
    return f"{num / total * 100:.0f}%"


def generate_json_summary(findings: dict, output_path: Path) -> None:
    """Save aggregated findings as JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(findings, f, indent=2)
    print(f"JSON summary saved to {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate summary report from scan results")
    parser.add_argument("-i", "--input", type=Path, required=True, help="Directory with *-scan.json files")
    parser.add_argument("-o", "--output", type=Path, default=Path("results/summary-report.md"))
    parser.add_argument("--json", type=Path, help="Also output JSON summary")
    args = parser.parse_args()

    findings = aggregate_results(args.input)
    generate_markdown_report(findings, args.output)

    if args.json:
        generate_json_summary(findings, args.json)

    print(f"\nSummary: {findings['safe_skills']}/{findings['total_skills']} skills safe")
    print(f"Total findings: {findings['total_findings']}")
