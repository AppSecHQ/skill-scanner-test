---
title: "False-positive register"
description: "A maintained list of scanner findings on skillscan.io that we believe are wrong, with the reason, so CRITICAL counts can be read with the right discount."
slug: false-positive-register
date: 2026-10-21
updated: 2026-10-21
tags: [false-positives, methodology, scanner-evaluation]
---

We do not delete findings. We record the ones we believe are wrong here, with reasoning, and annotate the skill page. This page is updated as the corpus grows and is hand-labelled, which makes it the only part of the dataset with human ground truth.

Status values: **confirmed FP** (we read the source and the finding is wrong), **likely FP** (pattern strongly suggests it; not fully reviewed), **disputed** (reported by a third party, under review).

## Pattern 1: detection signatures matched as attacks

The scanner's YARA and regex rules match strings regardless of context. A security tool that *looks for* `rm -rf /` is flagged as if it *runs* it.

| Skill | Source | Findings affected | Status | Reason |
|---|---|---|---|---|
| ClawDefender | clawhub.ai | 37 (22 CRITICAL) | confirmed FP | Pattern arrays in `clawdefender.sh` are quoted detection strings. ANSI color codes flagged as script injection. LLM and meta layers produced zero findings. [Full write-up](/research/2026/clawdefender-false-positives/). |
| yara-rule-authoring | organisation repo | 15 CRITICAL | likely FP | A guide to writing YARA rules necessarily contains the patterns YARA rules detect. |
| skill-scanner | cisco | 7 CRITICAL | likely FP | The scanner's own skill documents the signatures it uses. |
| qa-test-planner | organisation repo | 14 CRITICAL | likely FP | Test-planning examples include SQL injection and command injection test strings. |
| azure-eventhub-java | microsoft | 1 CRITICAL (`YARA_sql_injection`) | likely FP | SQL keyword patterns in documentation for a messaging SDK. |

## Pattern 2: security research tooling

Fuzzers, exploit harnesses, and cryptographic test suites contain attack-shaped code by design.

| Skill | Source | Findings affected | Status | Reason |
|---|---|---|---|---|
| constant-time-testing | trailofbits | 8 CRITICAL | likely FP | Timing-attack test harness; code reads like an attack because it tests resistance to one. |
| libafl | trailofbits | 4 CRITICAL | likely FP | Fuzzing framework integration. |

## Pattern 3: example data mistaken for payloads

| Skill | Source | Findings affected | Status | Reason |
|---|---|---|---|---|
| hugging-face-datasets | huggingface | 27 CRITICAL | likely FP | Example dataset-loading code and shell snippets in documentation; needs full review, the count is high enough that some may be real. |
| hugging-face-tool-builder | huggingface | 5 CRITICAL | likely FP | Same pattern. |

## Pattern 4: disclosed behaviour flagged as hidden

The LLM layer sometimes flags a behaviour that is documented in the skill. The meta layer usually downgrades these but keeps the severity label.

| Skill | Source | Finding | Status | Reason |
|---|---|---|---|---|
| 1inch | clawhub.ai | Hardcoded referral wallet (MEDIUM) | not FP, context | Fee is disclosed in docs. We keep it: users may not see the disclosure at activation. Listed here so readers know the dispute. |
| agent-wallet | clawhub.ai | Missing `wallet.py` as tool shadowing | confirmed FP | Meta layer: documentation error, low exploitability. |

## Running tally

As of 2026-10-21, findings labelled confirmed or likely FP: roughly 120 of 209 CRITICALs in the corpus, concentrated in ten skills. This is why the [results post](/research/2026/618-skills-full-scan/) says to read the CRITICAL count with a discount of about half. The remaining CRITICALs, mostly on ClawHub, we have not found reason to doubt.

## What would fix it

- Context-aware signature rules that distinguish string literals in detection arrays from executed commands. We will file this upstream with examples.
- Weighting: a signature hit with no corroborating LLM or behavioral finding should not be CRITICAL on its own. We may apply this as a displayed "adjusted severity" without altering the raw data.
- Allow-listing by skill purpose is tempting and wrong; a malicious skill could claim to be a security tool. Hand review stays.

## Disputing or adding an entry

Open an issue with the skill name, finding ID, and reasoning. Entries that are confirmed by reading source get **confirmed FP**; we would rather have more **likely** entries reviewed than fewer entries.
