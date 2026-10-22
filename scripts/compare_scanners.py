#!/usr/bin/env python3
"""Compare Cisco skill-scanner verdicts with NVIDIA SkillSpector verdicts on
the same skills.

Reads ``results/<name>-scan.json`` (Cisco) and
``results/skillspector/<name>-skillspector.json`` (SkillSpector) and writes
``results/scanner-comparison.json`` plus a Markdown summary.

Verdict normalisation (two tiers, because SkillSpector's CAUTION tier covers
most skills and Cisco's is_safe flips on any non-INFO finding):
  loose:  Cisco flagged = not is_safe;           SkillSpector flagged = recommendation != "SAFE"
  strict: Cisco flagged = max_severity >= HIGH;  SkillSpector flagged = recommendation == "DO_NOT_INSTALL" (score > 50)

Usage:
    python scripts/compare_scanners.py [--results results] [--md results/scanner-comparison.md]
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

SEVERITY_ORDER = ["SAFE", "INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"]


def _source_index(results: Path) -> dict[str, str]:
    """Map scan-file stems to the source attribution the published site uses.

    Older Cisco results do not carry ``source``; the site derives it at report
    time. ``docs/data/summary.json`` (one row per published scan) is the
    authority, keyed by its ``scan_file`` (``<stem>-scan.md``).
    """
    summary = results.parent / "docs" / "data" / "summary.json"
    if not summary.exists():
        return {}
    rows = json.loads(summary.read_text())
    rows = rows if isinstance(rows, list) else rows.get("skills", [])
    out = {}
    for r in rows:
        sf = r.get("scan_file") or ""
        if sf.endswith("-scan.md"):
            out[sf[: -len("-scan.md")]] = r.get("source")
    return out


def published_stem(stem: str) -> str:
    """The site publishes dot-prefixed scans (``.github-skills-*``) without the dot."""
    return stem.lstrip(".")


def skill_summary(results: Path) -> dict[str, dict]:
    """One compact SkillSpector verdict per scan stem, for the site.

    Keys match the published scan name (``docs/data/scans/<stem>-scan.json``),
    so dot-prefixed stems lose their dot. Includes every SkillSpector result,
    paired or not.
    """
    out = {}
    for ss_file in sorted((results / "skillspector").glob("*-skillspector.json")):
        stem = published_stem(ss_file.name[: -len("-skillspector.json")])
        ss = json.loads(ss_file.read_text())
        ra = ss.get("risk_assessment") or {}
        if not ra.get("recommendation"):
            continue  # scan errored
        issues = ss.get("issues") or []
        cats = Counter(i.get("category", "unknown") for i in issues)
        out[stem] = {
            "recommendation": ra.get("recommendation"),
            "score": ra.get("score"),
            "severity": ra.get("severity"),
            "issue_count": len(issues),
            "top_categories": [c for c, _ in cats.most_common(3)],
            "version": (ss.get("metadata") or {}).get("skillspector_version"),
            "mode": (ss.get("_meta") or {}).get("mode", "static"),
            "scanned_at": (ss.get("_meta") or {}).get("scanned_at"),
        }
    return out


def load_pairs(results: Path) -> list[dict]:
    pairs = []
    sources = _source_index(results)
    ss_dir = results / "skillspector"
    for cisco_file in sorted(results.glob("*-scan.json")):
        stem = cisco_file.name[: -len("-scan.json")]
        ss_file = ss_dir / f"{stem}-skillspector.json"
        if not ss_file.exists():
            continue
        cisco = json.loads(cisco_file.read_text())
        ss = json.loads(ss_file.read_text())
        if cisco.get("is_safe") is None:
            continue  # Cisco scan failed; nothing to compare
        ra = ss.get("risk_assessment", {})
        pairs.append({
            "name": stem,
            "skill_name": cisco.get("skill_name"),
            "source": cisco.get("source") or sources.get(published_stem(stem)),
            "cisco": {
                "flagged": not cisco["is_safe"],
                "flagged_strict": SEVERITY_ORDER.index(cisco.get("max_severity", "SAFE")) >= SEVERITY_ORDER.index("HIGH")
                if cisco.get("max_severity", "SAFE") in SEVERITY_ORDER else False,
                "max_severity": cisco.get("max_severity", "SAFE"),
                "findings": cisco.get("findings_count", 0),
                "categories": sorted({f.get("category", "unknown") for f in cisco.get("findings", [])}),
                "scanner_version": cisco.get("scanner_version"),
                "analyzers": cisco.get("analyzers_used", []),
            },
            "skillspector": {
                "flagged": ra.get("recommendation") != "SAFE",
                "flagged_strict": ra.get("recommendation") == "DO_NOT_INSTALL",
                "recommendation": ra.get("recommendation"),
                "score": ra.get("score"),
                "severity": ra.get("severity"),
                "findings": len(ss.get("issues", [])),
                "categories": sorted({i.get("category", "unknown") for i in ss.get("issues", [])}),
                "version": ss.get("metadata", {}).get("skillspector_version"),
            },
        })
    return pairs


def summarize(pairs: list[dict], key: str = "flagged") -> dict:
    n = len(pairs)
    both = sum(1 for p in pairs if p["cisco"][key] and p["skillspector"][key])
    cisco_only = sum(1 for p in pairs if p["cisco"][key] and not p["skillspector"][key])
    ss_only = sum(1 for p in pairs if not p["cisco"][key] and p["skillspector"][key])
    neither = n - both - cisco_only - ss_only
    agree = both + neither
    # Cohen's kappa on the binary flagged/not-flagged verdict
    pc = (both + cisco_only) / n if n else 0
    ps = (both + ss_only) / n if n else 0
    pe = pc * ps + (1 - pc) * (1 - ps)
    po = agree / n if n else 0
    kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0

    by_source: dict[str, Counter] = defaultdict(Counter)
    for p in pairs:
        cell = ("both" if p["cisco"][key] and p["skillspector"][key]
                else "cisco_only" if p["cisco"][key]
                else "skillspector_only" if p["skillspector"][key] else "neither")
        by_source[p["source"] or "unknown"][cell] += 1
        by_source[p["source"] or "unknown"]["total"] += 1

    return {
        "tier": key,
        "skills_compared": n,
        "flagged_by_cisco": both + cisco_only,
        "flagged_by_skillspector": both + ss_only,
        "flagged_by_both": both,
        "cisco_only": cisco_only,
        "skillspector_only": ss_only,
        "flagged_by_neither": neither,
        "agreement_rate": round(po, 4),
        "cohens_kappa": round(kappa, 4),
        "cisco_categories": Counter(c for p in pairs for c in p["cisco"]["categories"]).most_common(),
        "skillspector_categories": Counter(c for p in pairs for c in p["skillspector"]["categories"]).most_common(),
        "skillspector_recommendations": Counter(p["skillspector"]["recommendation"] for p in pairs).most_common(),
        "cisco_severities": Counter(p["cisco"]["max_severity"] for p in pairs).most_common(),
        "by_source": {k: dict(v) for k, v in sorted(by_source.items(), key=lambda kv: -kv[1]["total"])},
    }


def _tier_table(s: dict, title: str) -> list[str]:
    return [
        f"### {title}", "",
        "| | SkillSpector flagged | SkillSpector not flagged |",
        "|---|---|---|",
        f"| Cisco flagged | {s['flagged_by_both']} | {s['cisco_only']} |",
        f"| Cisco not flagged | {s['skillspector_only']} | {s['flagged_by_neither']} |",
        "",
        f"Agreement {s['agreement_rate']:.1%}, Cohen's kappa {s['cohens_kappa']:.2f}", "",
    ]


def render_markdown(summary: dict, strict: dict, pairs: list[dict]) -> str:
    s = summary
    lines = [
        "# Scanner comparison: Cisco skill-scanner vs NVIDIA SkillSpector (static)",
        "",
        f"Skills compared: {s['skills_compared']}. Both scanners ran without an LLM.",
        "",
        *_tier_table(s, "Loose tier: Cisco any finding vs SkillSpector CAUTION or DO_NOT_INSTALL"),
        *_tier_table(strict, "Strict tier: Cisco HIGH/CRITICAL vs SkillSpector DO_NOT_INSTALL"),
        "## By source (loose tier)",
        "",
        "| Source | Skills | Both | Cisco only | SkillSpector only | Neither |",
        "|---|---|---|---|---|---|",
    ]
    for src, c in s["by_source"].items():
        lines.append(f"| {src} | {c['total']} | {c.get('both', 0)} | {c.get('cisco_only', 0)} | {c.get('skillspector_only', 0)} | {c.get('neither', 0)} |")
    lines += ["", "## Cisco finding categories", "", "| Category | Skills |", "|---|---|"]
    lines += [f"| {c} | {n} |" for c, n in s["cisco_categories"]]
    lines += ["", "## SkillSpector finding categories", "", "| Category | Skills |", "|---|---|"]
    lines += [f"| {c} | {n} |" for c, n in s["skillspector_categories"]]
    lines += ["", "## Largest disagreements", "",
              "Skills one scanner rates most severely while the other calls safe.", "",
              "| Skill | Source | Cisco | SkillSpector |", "|---|---|---|---|"]
    disagree = [p for p in pairs if p["cisco"]["flagged"] != p["skillspector"]["flagged"]]
    disagree.sort(key=lambda p: -(SEVERITY_ORDER.index(p["cisco"]["max_severity"]) if p["cisco"]["max_severity"] in SEVERITY_ORDER else 0) - (p["skillspector"]["score"] or 0) / 20)
    for p in disagree[:40]:
        lines.append(f"| {p['skill_name']} | {p['source']} | {p['cisco']['max_severity']} ({p['cisco']['findings']}) | {p['skillspector']['recommendation']} {p['skillspector']['score']} ({p['skillspector']['findings']}) |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", type=Path, default=Path("results"))
    ap.add_argument("--json", type=Path, default=None, help="default: <results>/scanner-comparison.json")
    ap.add_argument("--md", type=Path, default=None, help="default: <results>/scanner-comparison.md")
    args = ap.parse_args()
    pairs = load_pairs(args.results)
    summary = summarize(pairs)
    strict = summarize(pairs, "flagged_strict")
    out_json = args.json or args.results / "scanner-comparison.json"
    out_md = args.md or args.results / "scanner-comparison.md"
    out_json.write_text(json.dumps({"summary": summary, "summary_strict": strict, "skills": pairs}, indent=1))
    out_md.write_text(render_markdown(summary, strict, pairs))
    per_skill = skill_summary(args.results)
    out_skills = args.results / "skillspector-summary.json"
    out_skills.write_text(json.dumps(per_skill, indent=1, sort_keys=True))
    print(f"wrote {out_skills} ({len(per_skill)} skills)")
    print(f"{summary['skills_compared']} skills; agreement {summary['agreement_rate']:.1%}, kappa {summary['cohens_kappa']:.2f}; "
          f"both {summary['flagged_by_both']}, cisco-only {summary['cisco_only']}, skillspector-only {summary['skillspector_only']}, neither {summary['flagged_by_neither']}")
    print(f"strict: agreement {strict['agreement_rate']:.1%}, kappa {strict['cohens_kappa']:.2f}; "
          f"both {strict['flagged_by_both']}, cisco-only {strict['cisco_only']}, skillspector-only {strict['skillspector_only']}, neither {strict['flagged_by_neither']}")
    print(f"wrote {out_json} and {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
