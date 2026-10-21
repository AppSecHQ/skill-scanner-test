---
title: "Reading a skillscan.io report"
description: "How to interpret a skill page on skillscan.io: the verdict, severity levels, finding categories, analyzer sources, confidence, and scan history."
slug: reading-a-skillscan-report
order: 4
updated: 2026-10-21
---

Every skill page has the same layout. This page explains each part.

## Verdict strip

**SAFE** or **ISSUES FOUND**, the maximum severity, the source registry, the date of the last scan, and the number of scans. SAFE is the scanner's own threshold decision and a SAFE skill can still have MEDIUM or LOW findings worth reading. The verdict is not a human judgement.

## Summary

When the LLM analyzer ran, its overall assessment of the skill is shown as a paragraph. This is the fastest way to understand what the skill does and what concerned the analyzer. Community-requested scans run without the LLM layer and have no summary.

## Severity

| Level | Meaning |
|---|---|
| CRITICAL | A pattern that, if real, gives an attacker code execution, credentials, or data. Read the snippet. |
| HIGH | Serious and likely exploitable in normal use. |
| MEDIUM | Risky design or disclosure problem; often legitimate functionality with a real cost. |
| LOW | Hygiene: missing license, unpinned version, loose wording. |
| INFO | Observations with no direct risk. |

## Findings

Each finding shows its category (linked to the [category page](/categories/)), the rule or analyzer that produced it, the file and line, a snippet, a description, and remediation text. Two fields matter most:

- **Analyzer.** `static` findings are signature matches and have the highest false-positive rate. `llm` and `behavioral` findings reflect a reading of the whole file. `meta` fields on an LLM finding show whether a second pass confirmed it.
- **Confidence and exploitability** (LLM findings only). A finding marked validated with low exploitability is usually a documentation or disclosure issue, not an attack.

## What we checked and did not check

Lists the analyzers that ran and the standing blind spots: no execution, no runtime-fetched content, no archive expansion, no image text. See [methodology](/methodology/).

## Scan history

Every scan of this skill, with finding count and max severity. A change between scans means the skill changed, the scanner changed, or both. The scanner version is recorded on each run so you can tell which.

## Links

The registry page, the source repository at the scanned commit, and the raw JSON for this skill. The JSON is the authoritative record; the page is a rendering of it.

## Disputing a finding

Open an issue in the [repository](https://github.com/AppSecHQ/skill-scanner-test/issues) with the skill name and finding ID. We do not delete findings. Confirmed false positives are listed in the [register](/research/2026/false-positive-register/) and annotated on the skill page.
