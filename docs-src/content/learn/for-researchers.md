---
title: "For researchers: using the skillscan.io dataset"
description: "How to download, cite, and reproduce the skillscan.io dataset of AI agent skill security scan results, including schema, history, and known caveats."
slug: for-researchers
order: 5
updated: 2026-10-21
---

The dataset behind this site is public, versioned by scan run, and intended to be cited. This page is the short guide; the [data page](/data/) has the download and license.

## What is in it

- One JSON record per skill per scan run, with every finding: rule ID, category, severity, file, line, snippet, description, remediation, analyzer, and for LLM findings the model, overall assessment, and meta-validation fields.
- A summary per run: counts by severity, by category, by source, and the top risks.
- The category taxonomy with its mapping to OWASP AST10.
- Scan history per skill across runs, including scanner version.
- The original skill sources are not redistributed. Each record links to the repository and commit that was scanned.

## What it is good for

- Studying the distribution of finding types across registries and over time.
- Measuring drift: skills whose findings changed between scans, including those that went from clean to flagged after an update.
- Evaluating scanner behaviour on real registry content rather than synthetic test cases. The [false-positive register](/research/2026/false-positive-register/) is hand-labelled.
- Cross-referencing with published incident reports. The ClawHavoc campaign is a worked example.

## What it is not good for

- Ground truth. The labels are scanner output. Only the false-positive register has human labels.
- A random sample. See the selection notes in [methodology](/methodology/).
- Runtime behaviour. Nothing was executed.

## Reproducing

The pipeline is Python and lives in the [repository](https://github.com/AppSecHQ/skill-scanner-test). Each record names the scanner version and, for LLM findings, the model. Re-running the static, behavioral, bytecode, and trigger analyzers on the linked commit should reproduce those findings exactly. LLM findings will vary between runs.

## Citing

A `CITATION.cff` is in the repository root. Cite the dataset with the scan run date you used, since the corpus changes between runs.

## Contributing

Corrections to the false-positive register, additional registries, and additional scanners run over the same corpus are the most useful contributions. Open an issue first.
