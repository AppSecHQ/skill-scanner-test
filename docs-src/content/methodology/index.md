---
title: "Methodology and limitations"
description: "How skillscan.io scans AI agent skills, which analyzers run, how often, what the pipeline cannot see, and which known scanner bypasses apply to it."
order: 1
updated: 2026-10-21
---

This page describes exactly what produces the results on this site, so you can decide how much weight to give them. Short version: every result here is the output of one open-source scanner run in its fullest configuration, published as-is, with a second-pass validation layer, and with the gaps listed below.

## What we scan

Skills are cloned from public registries and repositories and scanned from the local checkout. Current coverage, as of the scan run dated 2026-05-09:

| Source | Skills |
|---|---|
| clawhub.ai (OpenClaw registry) | 315 |
| Microsoft skills repo | 107 |
| skills.sh (Vercel registry, top installs) | 74 |
| Trail of Bits skills | 49 |
| hoodini/ai-agents-skills | 27 |
| Anthropic skills | 17 |
| Hugging Face skills | 9 |
| Other individual repos | 20 |

That is 618 distinct skills across 650 scan records; thirty skills were scanned more than once with different analyzer sets, and each skill's page shows every run.

Selection is not random. skills.sh skills were chosen by install count. ClawHub skills were taken in bulk. Organisation repos were added because they are widely installed. Treat cross-registry comparisons as indicative, not as a controlled sample.

## What runs

The scanner is Cisco AI Defense [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner), pinned to a specific version recorded in each scan result. All analyzers are enabled:

| Analyzer | What it does |
|---|---|
| static | YAML and YARA signatures over all files: known attack strings, suspicious commands, credential shapes, encoding |
| behavioral | Data-flow tracing through bundled scripts, looking for source-to-sink paths such as env var to network |
| bytecode | Inspects compiled Python artifacts rather than skipping them |
| trigger | Checks the skill's name and description for discovery hijacking and over-broad triggers |
| llm | An LLM reads the whole skill and writes findings with description, snippet, and remediation |
| meta | A second LLM call re-validates each LLM finding against the source and assigns confidence, exploitability, and impact |
| pipeline | Orchestration; records which analyzers ran |

The LLM and meta layers use the model named in each finding's metadata. Community-requested scans run without the LLM layers for cost and secret-handling reasons, and their pages say so.

## How often

Scans run on demand from this repository's workflow and whenever a community scan request is approved. Each run writes a dated result. Skill pages keep every run, so you can see whether a verdict changed between scans. The site does not yet re-scan the full corpus on a fixed schedule; the per-skill "last scanned" date is the thing to check.

## What a verdict means

A skill is marked **SAFE** when the scanner reports `is_safe: true`. That flag is set by the scanner's own severity threshold, which is why a skill can be SAFE and still carry MEDIUM findings. **ISSUES FOUND** means at least one finding crossed the threshold. Neither label is a judgement by a human. We do not remove findings we believe are wrong; we list them in the [false-positive register](/research/2026/false-positive-register/) and leave the record intact.

## What we cannot see

Be specific about this, because it determines what the site is good for.

- **Runtime behaviour.** We never execute a skill. Anything that only misbehaves when run, or when a particular tool is present, is invisible to us.
- **Content fetched at runtime.** If a skill tells the agent to read a URL, we scan the instruction, not the URL. The remote content can change after our scan. This is OWASP AST05 and AST07 territory and it is the single largest blind spot.
- **Non-English and image-borne text.** The static rules are English-centric. The LLM layer handles other languages inconsistently. Text in images is not read at all.
- **Dependencies installed by the skill.** A `pip install` or `npm install` in a skill's instructions pulls code we did not scan.
- **Composition.** Each skill is scored alone. Two skills that are individually benign and jointly harmful will both show as SAFE. The CompoSkill and ColluSkill papers describe this class.
- **Registry metadata.** Author reputation, publish history, download counts, and signing status are not inputs to the verdict.

## Known bypasses that apply to this pipeline

In June 2026 Trail of Bits published bypasses for Cisco skill-scanner, ClawHub's detector, and the three scanners integrated into skills.sh. The Cloud Security Alliance summarised the classes. Our position on each:

| Bypass class | Status here |
|---|---|
| Whitespace inflation past scanner context limits | Partially mitigated: file size and whitespace ratio are visible on the skill page, but the LLM layer still truncates. Flagged under `obfuscation` only when the static rules catch it. |
| Precompiled Python bytecode | Mitigated by the bytecode analyzer, within its signature coverage. |
| Archive and document indirection | Not mitigated. Archives inside a skill are not expanded. |
| Social engineering of the LLM judge | Not mitigated. A persuasively framed skill can get its severity downgraded. The meta layer reduces but does not remove this. |
| Multimodal hidden instructions | Not mitigated. |

We do not claim these results are a safety guarantee. They are a lower bound on what is wrong with a skill, produced consistently across a large corpus, with the history kept.

## Reproducing a result

Every skill page links to its raw JSON. The scanner version, analyzers, and model are in that file. The pipeline scripts are in the [repository](https://github.com/AppSecHQ/skill-scanner-test). See [For researchers](/learn/for-researchers/) for the dataset and citation.
