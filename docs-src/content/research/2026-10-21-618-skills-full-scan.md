---
title: "618 skills, 650 scans, two registries: what a full LLM and meta scan shows"
description: "Results from scanning 618 distinct AI agent skills (650 scans) from ClawHub, skills.sh, and major skill repos with every analyzer enabled: 22% flagged, ClawHub far ahead, and most CRITICALs in a handful of security tools."
slug: 618-skills-full-scan
date: 2026-10-21
tags: [results, clawhub, skills.sh, registry-comparison]
---

This is the state of the corpus as of the scan run dated 2026-05-09, the first run where every skill went through the full pipeline: static, behavioral, bytecode, trigger, LLM, and meta-validation. The data is on the [dataset page](/data/).

## Totals

The run contains 650 scan records. Thirty skills were scanned more than once with different analyzer sets, so the corpus is 618 distinct skills. Figures below use the fullest scan of each skill; the raw run totals (650 records, 1,381 findings, 142 flagged) are in `summary.json`.

| | Count |
|---|---|
| Distinct skills | 618 |
| Scan records | 650 |
| Issues found | 139 (22%) |
| Findings (deduplicated) | 1,361 |
| CRITICAL / HIGH / MEDIUM / LOW (raw run) | 209 / 251 / 714 / 180 |

## By source

| Source | Skills | Issues found | Max CRITICAL | Findings |
|---|---|---|---|---|
| clawhub.ai | 315 | 120 (38%) | 61 | 830 |
| skills.sh (top installs) | 74 | 5 (7%) | 1 | 78 |
| Microsoft | 107 | 2 | 1 | 31 |
| Trail of Bits | 49 | 5 | 5 | 72 |
| Anthropic | 17 | 1 | 0 | 12 |
| hoodini/ai-agents-skills | 27 | 2 | 1 | 43 |
| Hugging Face | 9 | 2 | 2 | 267 |
| Others | 20 | 2 | 2 | 28 |

Two things stand out. First, the registry gap is large: a ClawHub skill was more than five times as likely to be flagged as a top skills.sh skill. This matches Snyk's February finding that curated skills.sh skills show negligible CRITICALs, and the direction of the arXiv 238k-skill study, though our numbers are not comparable to either because of selection. Second, the organisation repos are mostly clean but not spotless, and the CRITICALs there are instructive, as the next section shows.

## Where the CRITICALs are

209 CRITICAL findings sounds alarming. By category they are command injection (114), data exfiltration (59), hardcoded secrets (21), social engineering (8), prompt injection (5), and resource abuse (2). By skill, they concentrate:

| Skill | CRITICALs | What it is |
|---|---|---|
| hugging-face-datasets | 27 | Dataset tooling with example code |
| zoho-email | 18 | ClawHub email integration |
| yara-rule-authoring | 15 | A guide to writing YARA rules |
| qa-test-planner | 14 | Test planning with injection examples |
| constant-time-testing | 8 | Trail of Bits cryptographic test tooling |
| skill-scanner | 7 | The scanner's own skill |
| hugging-face-tool-builder | 5 | |
| meta-ads | 5 | ClawHub |
| update-plus | 5 | ClawHub |
| libafl | 4 | Trail of Bits fuzzing |

Ten skills account for 108 of 209 CRITICALs, and at least five of those ten are security or testing tools whose job is to contain attack patterns. Our reading is that **roughly half of all CRITICALs in the corpus are signature matches on legitimate security content**. We have started a [false-positive register](/research/2026/false-positive-register/) to label these one by one instead of adjusting the numbers.

The other half is real. The ClawHub CRITICALs include the [ClawHavoc campaign](/research/2026/clawhavoc-validation/) skills, install scripts that download and execute from unpinned GitHub URLs, and credential handling that writes API keys to plaintext files.

## The LLM layer

The LLM analyzer produced findings with readable descriptions and remediation, and its meta-validation confirmed about 60 percent at high confidence, 40 percent at medium, and none at low. The medium cases are mostly downgrades for context: a referral wallet that is disclosed in the docs, a missing file that is a documentation error. The LLM layer never once flagged the security-tool skills above as CRITICAL; the signatures did. This is the strongest argument for weighting analyzer source when reading a page.

## By category, whole corpus

Data exfiltration (423), command injection (211), social engineering (168), transitive trust abuse (151), unauthorized tool use (133), policy violation (91), resource abuse (88), prompt injection (53), tool chaining abuse (30), hardcoded secrets (23), skill discovery abuse (6), obfuscation (3), autonomy abuse (1). Each links to a [category page](/categories/) with examples.

The low prompt injection count deserves a note. It does not mean injection is rare. It means the scanner's prompt-injection rules are narrow and most injection-shaped content lands under social engineering or policy violation. The near-zero obfuscation count is a known blind spot, not good news; the bypass classes Trail of Bits documented would not raise it.

## What changed since the last post

The February run covered 585 scan records. This run adds the Microsoft repo, more ClawHub, and re-scans everything with the pinned scanner version, which is now recorded in every result. Skill pages show both runs.

## Next

Re-scan on a schedule and publish drift. Add a second scanner over the same corpus. Expand the false-positive register. If you want a skill scanned, [request it](/request-a-scan/).
