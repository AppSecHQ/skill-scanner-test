---
title: "Two scanners, one corpus: Cisco skill-scanner and NVIDIA SkillSpector on 1,302 skills"
description: "We ran NVIDIA's SkillSpector in static mode over every skill the Cisco scanner had already scanned. At the strict tier the two agree 80% of the time with kappa 0.26; at the loose tier kappa is 0.07. Where they disagree, and what a second verdict does and does not tell you."
slug: two-scanners-one-corpus
date: 2026-10-22
tags: [results, scanner-evaluation, skillspector, methodology]
---

The [full-scan post](/research/2026/618-skills-full-scan/) ended with a promise to add a second scanner over the same corpus. This is that. Every skill on this site now has two verdicts: one from Cisco's `skill-scanner` 2.3.1, which has been the backbone of the project, and one from NVIDIA's [SkillSpector](https://github.com/NVIDIA/skillspector) 2.12.0. Both ran without a language model, so the comparison cost nothing to produce and anyone can reproduce it from the [dataset](/data/).

The short version: the two scanners agree on the extreme cases and disagree on nearly everything in between. That is the same result the [seven-scanner study](https://theweatherreport.ai/posts/skill-scanner-disagreement/) of 238,180 skills reported, now reproduced on a corpus with hand-labelled false positives in it.

## Setup

| | Cisco skill-scanner | NVIDIA SkillSpector |
|---|---|---|
| Version | 2.3.1 | 2.12.0 |
| Mode | Static, behavioral, trigger; LLM and meta layers on the older full-scan runs | Static only (`--no-llm`) |
| Verdict scale | `is_safe` plus a max severity: INFO, LOW, MEDIUM, HIGH, CRITICAL | Score 0 to 100, banded into SAFE (0 to 20), CAUTION (21 to 50), DO_NOT_INSTALL (51 and up) |
| Skills compared | 1,302 | 1,302 |
| Cost | 0 tokens | 0 tokens, about 3 seconds per skill |

The two scales do not line up, so we compare at two tiers. The **loose tier** asks whether each scanner raised anything at all: Cisco `is_safe` false against SkillSpector CAUTION or DO_NOT_INSTALL. The **strict tier** asks whether each scanner would tell you not to install: Cisco HIGH or CRITICAL against SkillSpector DO_NOT_INSTALL. Agreement is the share of skills where both said yes or both said no. Cohen's kappa corrects that for chance, so two scanners that flag everything would score 100% agreement and kappa 0.

## The headline

Strict tier:

| | SkillSpector: do not install | SkillSpector: anything else |
|---|---|---|
| **Cisco HIGH or CRITICAL** | 82 | 129 |
| **Cisco below HIGH** | 135 | 956 |

Agreement 79.7%, kappa 0.26.

Loose tier:

| | SkillSpector: CAUTION or worse | SkillSpector: SAFE |
|---|---|---|
| **Cisco flagged** | 189 | 22 |
| **Cisco clean** | 795 | 296 |

Agreement 37.2%, kappa 0.07.

A kappa of 0.26 is "fair" on the usual scale. For two tools that both claim to tell you whether a skill is safe to install, it means that if one of them says no, the other one agrees less than half the time. Of the 106 skills Cisco rates CRITICAL, SkillSpector tells you not to install 48.

## Why the loose tier collapses

SkillSpector says CAUTION about 767 of the 1,302 skills. That is not because it found something in 767 skills. 256 of those CAUTION verdicts carry a score of zero and no issues at all.

The reason is in the scanner's design. When SkillSpector's deterministic layer cannot fully inspect a package, it fails closed: a SAFE verdict is downgraded to CAUTION with a record of what was left unread. In 250 of those 256 results the record says `reference_missing`: the SKILL.md refers to a file or path that is not in the package, so the scanner could not follow the instruction to its target. The rest are parse limits on large files, two syntax errors, and two cases of "obfuscated instruction text", one of which is ordinary prose with Unicode punctuation. The remaining CAUTION verdicts have scores in the low tens from a handful of low-severity pattern hits.

So in static mode, SkillSpector's middle band is closer to "this has text I did not finish reading" than to "this is risky". That is a defensible choice for a scanner. It is a poor signal for a comparison, which is why the strict tier is the one to read.

## Where they disagree

**Cisco says HIGH or CRITICAL, SkillSpector does not: 129 skills.** SkillSpector put 107 of them at CAUTION and 22 at SAFE. The Cisco findings behind them are dominated by data exfiltration (93 skills), social engineering (72), and command injection (71). Ninety-one of the 129 are ClawHub skills. This is the ClawHub-heavy tail of the Cisco results, and a lot of it is signature matches on install scripts and credential handling.

**SkillSpector says do not install, Cisco does not: 135 skills.** Cisco rated 73 of them clean and 49 MEDIUM. SkillSpector's reasons are privilege escalation (77), analysis evasion (69), excessive agency (64), least-privilege violations in MCP configuration (58), and tool misuse (57). These are spread across Microsoft (33), ClawHub (32), and the K-Dense scientific skills (27). The analysis-evasion and least-privilege categories have no counterpart in the Cisco taxonomy, which is most of the explanation: SkillSpector is answering a question Cisco does not ask.

**Both say stop: 82 skills.** ClawHub 31, K-Dense 13, Microsoft 11, the heygen hyperframes video toolkit 6. These are the skills we would send a reader to first.

Seventy-seven skills score exactly 100 on SkillSpector. The score saturates, so inside the DO_NOT_INSTALL band there is no ranking to read.

## The false-positive register, scored twice

We keep a [register](/research/2026/false-positive-register/) of Cisco findings we believe are wrong, mostly security tools whose detection signatures match the scanner's own rules. A second scanner is the obvious test: does it make the same mistakes?

| Skill | Cisco | SkillSpector | Verdict on the verdicts |
|---|---|---|---|
| ClawDefender | 37 CRITICAL static; 0 after LLM re-scan | DO_NOT_INSTALL, score 100, 50 issues | SkillSpector repeats the signature false positive that Cisco's LLM layer cleared |
| yara-rule-authoring | 19 CRITICAL | DO_NOT_INSTALL, 100 | Both match the YARA examples as attacks |
| skill-scanner (Cisco's own skill) | 19 CRITICAL static; 0 after re-scan | DO_NOT_INSTALL, 100 | Same |
| qa-test-planner | 22 CRITICAL | DO_NOT_INSTALL, 57 | Same |
| hugging-face-datasets | 78 CRITICAL | DO_NOT_INSTALL, 78 | Same |
| constant-time-testing | 12 CRITICAL | CAUTION, score 0 | SkillSpector does not see the timing-attack harness as an attack |
| libafl | 8 CRITICAL | CAUTION, 25 | Mostly clears it |
| azure-eventhub-java | 5 CRITICAL | CAUTION, 0 | Clears it |

Two scanners built on pattern matching agree with each other on the pattern-matching mistakes. Agreement between scanners is not evidence that a finding is real when both are reading the same strings. The three cases where SkillSpector clears a Cisco false positive are all code-heavy security tooling, where its component-level analysis has something to work with that a YARA rule on documentation does not.

Two newer register entries go the other way. The flowkit-labs `reddit-automation` skill is CRITICAL on Cisco for the phrase "ignore your instructions", which appears in a paragraph telling the agent to treat Reddit content as untrusted and to disregard exactly that phrase. SkillSpector gives it a score of zero. The mattpocock `implement` skill is HIGH on Cisco for "fetch it from the issue tracker and state its title", read as acquiring and executing remote content. SkillSpector rates it SAFE. In both cases the second scanner is right, and in both cases the right answer came from not having a rule rather than from having a better one.

## Largest disagreements

Skills one scanner rates as severely as it can while the other stays at MEDIUM or below. The table runs one way because SkillSpector's score saturates at 100 so often; the other direction is shorter but exists. Eight skills Cisco rates CRITICAL get SkillSpector's SAFE: activecampaign, ci-gen, crypto-wallet, polymarket, save-money, sendclaw, x-trends, and telegram-pairing-customization, all on ClawHub, each with three to seven Cisco findings. Fourteen more are HIGH against SAFE.

| Skill | Source | Cisco | SkillSpector |
|---|---|---|---|
| azure-prepare | microsoft | MEDIUM, 5 findings | 100, 69 issues |
| foundry-iq | microsoft | MEDIUM, 2 | 100, 50 |
| paper-lookup | K-Dense-AI | MEDIUM, 7 | 100, 57 |
| dev-browser | sawyerhood | MEDIUM, 7 | 100, 41 |
| hugging-face-evaluation | huggingface | MEDIUM, 96 | 100, 35 |
| testing-handbook-generator | trailofbits | MEDIUM, 3 | 100, 14 |
| earnings-calendar | clawhub.ai | MEDIUM, 2 | 100, 7 |
| writing-skills | skills.sh | MEDIUM, 2 | 100, 21 |

The Microsoft rows are the ones to watch. SkillSpector reports privilege escalation and excessive agency in the Azure deployment and Foundry skills, where Cisco's own cross-file analysis also found environment-variable exfiltration chains at CRITICAL in the newer scans. We have not finished reading those by hand and are not publishing a verdict on them yet.

## What a second verdict is worth

Three things we now believe, having run both:

- **Agreement is a weak signal and disagreement is a strong one.** When both scanners say stop, you still have to read the skill, because both can be fooled by the same strings. When they disagree at the strict tier, one of them has a blind spot, and the 264 skills in that position are the most useful thing this comparison produced.
- **Taxonomies do not map.** Many of SkillSpector's strict-tier-only flags are categories Cisco does not have. A "second opinion" from a scanner with a different threat model is not a second opinion on the same question.
- **Static verdicts are rules, and rules have an author.** Both scanners' mistakes trace to a specific pattern someone wrote. The [Pretext](https://arxiv.org/abs/2609.39607) evasion work got past SkillSpector 97% of the time with rewrites that preserve meaning; it would get past Cisco's YARA rules the same way. Neither number here should be read as a detection rate.

Every skill page will show both verdicts, and the full comparison, including every pair, is in `scanner-comparison.json` on the [dataset page](/data/).

## Method and limits

SkillSpector was installed from its GitHub repository (it is not on PyPI) and run per skill with `scan --no-llm --format json`. A non-zero exit code of 1 means a score above 50 and is a result, not an error. One skill could not be resolved to a local path and is excluded. The Cisco results are the published ones: the February corpus was scanned with every analyzer including the LLM layers, the K-Dense and October additions with static, behavioral, and trigger analyzers only. That mix favours Cisco slightly, since some of its clean verdicts came from a model reading the code. Kappa is computed over the 1,302 paired skills. Three byte-identical copies of one skill collection (86 skills each) are in the corpus and are counted three times; they agree with themselves, so they inflate agreement by a small amount in both tiers.

## Next

Show both verdicts on every skill page. Add a third column from a scanner with a different design, most likely Snyk Agent Scan. Hand-review the 264 strict-tier disagreements and move the clear cases into the register. Re-run SkillSpector with a model on the disagreements only, which is where tokens buy the most.
