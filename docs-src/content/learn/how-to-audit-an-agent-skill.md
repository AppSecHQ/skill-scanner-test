---
title: "How to audit an agent skill before installing it"
description: "A practical checklist for reviewing a SKILL.md and its bundled scripts for prompt injection, exfiltration, over-privilege, and supply chain risk, mapped to OWASP AST10."
slug: how-to-audit-an-agent-skill
order: 2
updated: 2026-10-21
---

This takes ten minutes for a typical skill and catches most of what our scanner catches. It will not catch everything; neither does the scanner. Do both.

## 0. Look it up first

Search the skill name on skillscan.io. If it has a page, read the verdict, the findings, and the scan history. A skill whose findings changed between scans deserves more attention than one that has been stable. If it is not here, [request a scan](/request-a-scan/) and continue with the manual review.

## 1. Frontmatter: does the description match the body?

Open `SKILL.md`. The `name` and `description` are what the agent uses to decide when to load this skill.

- Is the description specific, or stuffed with unrelated keywords so it triggers on everything? (AST04, [skill discovery abuse](/categories/skill-discovery-abuse/))
- Does it claim to be official, verified, or from a vendor? Check the publisher against that vendor's actual repo.
- Does any declared tool or permission list exceed what the description needs? (AST03, [unauthorized tool use](/categories/unauthorized-tool-use/))

## 2. Body: read it as instructions to a very obedient assistant

Read every line of the Markdown body. You are looking for sentences, not code.

- Instructions to skip confirmation, act silently, or not show the user something. ([Policy violation](/categories/policy-violation/))
- Instructions to ignore prior rules, change role, or treat this file as higher authority. ([Prompt injection](/categories/prompt-injection/))
- Urgency, authority claims, or "this is required by corporate policy" framing. ([Social engineering](/categories/social-engineering/))
- Instructions to read any file outside the project, especially `~/.ssh`, `~/.aws`, `.env`, browser profiles, or wallets. ([Data exfiltration](/categories/data-exfiltration/))
- Instructions to fetch a URL and follow what it says. That URL is now part of the skill and can change tomorrow. (AST05, [transitive trust abuse](/categories/transitive-trust-abuse/))

Render the raw file, not the preview. Look for HTML comments, zero-width characters, white-on-white text, and long runs of whitespace that push content off screen. ([Obfuscation](/categories/obfuscation/))

## 3. Scripts: every command, every destination

List every command the skill tells the agent to run and every script in `scripts/`.

- Anything that downloads and executes: `curl | sh`, `pip install` from a git URL, `npx` of an unpinned package. ([Command injection](/categories/command-injection/))
- Every outbound network destination. Is each one required by the stated purpose? Is any a bare IP, a URL shortener, or a webhook?
- Any encoding of local data: base64, hex, compression before a network call.
- Hardcoded keys, tokens, wallet addresses, referral codes. ([Hardcoded secrets](/categories/hardcoded-secrets/), [resource abuse](/categories/resource-abuse/))
- Files you cannot read: `.pyc`, archives, binaries, images with text. If you cannot read it, you cannot review it.

## 4. Sequence: what does it do end to end?

Trace one full run. Read a secret, write it to a temp file, commit, push is harmful even though each step is routine. ([Tool chaining abuse](/categories/tool-chaining-abuse/))

## 5. Persistence and autonomy

Does the skill install other skills, schedule itself, modify agent configuration, or write to memory so it persists across sessions? ([Autonomy abuse](/categories/autonomy-abuse/))

## 6. Provenance

Who published it? How many other skills do they have, and when did they appear? Is the repository the one the registry links to? Pin a commit, not a branch. (AST02, AST07)

## Decision

- Any instruction to hide actions, override rules, or exfiltrate: do not install, and report it to the registry.
- Remote fetch-and-execute from an unpinned source: do not install until pinned, or vendor the script.
- Over-broad permissions with a plausible reason: install in a sandbox with the permissions reduced.
- Clean: install, pin, and re-check when it updates.

For the longer form of this list, see the [OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/) checklist.
