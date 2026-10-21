---
title: "About skillscan.io"
description: "skillscan.io publishes continuous security scan results for AI agent skills from public registries such as skills.sh and ClawHub, with per-skill pages and history."
order: 1
updated: 2026-10-21
---

skillscan.io scans AI agent skills from public registries and publishes what the scanner finds, per skill, with history. The goal is a public, reproducible record of the state of the skill supply chain that anyone can check before installing something and that researchers can build on.

## What this site is

- A continuously updated dataset of scan results for skills from skills.sh, ClawHub, and widely installed organisation repositories.
- A page per skill with verdict, findings, remediation text, and a timeline of every scan.
- Category pages that map the scanner's finding types to the [OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/).
- A research log of what we observe, including where the scanner is wrong.

## What this site is not

- Not a security guarantee. Read the [methodology and limitations](/methodology/).
- Not a registry. We do not host or distribute skills. Install from the source linked on each page.
- Not affiliated with any scanner vendor. We run Cisco's open-source skill-scanner because it is open and runs locally. Other scanners may be added to the same corpus.

## Name clarification

There are other things called SkillScan. **skillscan.sh** is an independent benchmark that measures how well different scanners detect attacks; we scan the registries themselves, and the two are complementary. **SkillScan** is also a long-standing career skills assessment product with no connection to this site. And `skillscan` on PyPI is a separate command-line tool.

## Who runs it

This is a project of AppSecHQ, maintained in the open at [github.com/AppSecHQ/skill-scanner-test](https://github.com/AppSecHQ/skill-scanner-test). The site, pipeline, and tests are MIT licensed. The dataset is CC BY 4.0. Report problems, request a scan, or dispute a finding through GitHub Issues.
