---
title: "Dataset"
description: "Download the skillscan.io dataset: per-skill security scan results for AI agent skills from skills.sh, ClawHub, and major skill repositories, with schema, license, and citation."
order: 1
updated: 2026-10-21
---

All scan results on this site are available as data.

## Download

| File | Contents |
|---|---|
| `/data/summary.json` | Current run: totals, severity and category counts, per-skill index, top risks, analyzers used |
| `/data/scans/<slug>-scan.json` | Full findings for one skill, current run |
| `/data/categories.json` | Category taxonomy with OWASP AST10 mapping and definitions |
| Repository `results/` | Every run, JSON and Markdown, with scanner version |

A CSV export of the per-skill index and a single-file archive of all scan JSON are planned; until then, clone the [repository](https://github.com/AppSecHQ/skill-scanner-test).

## Schema

Per-skill record (abridged):

```json
{
  "skill_name": "...",
  "is_safe": true,
  "max_severity": "MEDIUM",
  "findings_count": 2,
  "scanner_version": "2.3.1",
  "analyzers_used": ["static_analyzer", "llm_analyzer", "meta_analyzer"],
  "timestamp": "2026-05-09T01:44:52",
  "findings": [{
    "id": "...", "rule_id": "LLM_DATA_EXFILTRATION",
    "category": "data_exfiltration", "severity": "MEDIUM",
    "title": "...", "description": "...", "file_path": "SKILL.md",
    "line_number": null, "snippet": "...", "remediation": "...",
    "analyzer": "llm",
    "metadata": { "model": "...", "overall_assessment": "...",
                  "validated": true, "confidence": "HIGH",
                  "exploitability": "Low", "impact": "..." }
  }]
}
```

Category slugs are the thirteen in `categories.json`. Severity is one of CRITICAL, HIGH, MEDIUM, LOW, INFO.

## License

The dataset (scan results, summaries, taxonomy) is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The pipeline and site code are MIT. Skill source code is not redistributed and remains under its own license at the linked repository. Finding text includes snippets quoted from scanned skills for identification.

## Citation

```
AppSecHQ. skillscan.io: Security scan results for AI agent skills. Dataset, scan run YYYY-MM-DD. https://skillscan.io/data/
```

A machine-readable `CITATION.cff` is in the repository root. Please include the scan run date, because the corpus changes.

## Caveats

Labels are scanner output, not ground truth. Selection is not random. Nothing was executed. Read the [methodology](/methodology/) before drawing conclusions, and the [false-positive register](/research/2026/false-positive-register/) before counting CRITICALs.
