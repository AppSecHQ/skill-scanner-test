---
title: "Agent skill scanners compared"
description: "A neutral comparison of AI agent skill security scanners, including Cisco skill-scanner, Snyk Agent Scan, SkillSpector, and registry-integrated checks, with observations from running one at scale."
order: 1
updated: 2026-10-21
---

This page lists the scanners we know of, what each does, and what we have observed. We run Cisco's scanner for this site. We are not affiliated with any vendor. For measured detection rates, use the independent benchmark at [skillscan.sh](https://skillscan.sh/); this page is about scope and behaviour, not scores.

| Scanner | Type | Open source | Runs locally | LLM layer | Notes |
|---|---|---|---|---|---|
| [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) | Static + behavioral + bytecode + trigger + LLM + meta | Yes | Yes | Optional | What this site runs. Full pipeline, high signature false-positive rate, meta layer helps. |
| [Snyk Agent Scan](https://snyk.io/) (formerly Invariant mcp-scan) | Environment inventory + LLM | Partly | CLI | Yes, cloud | Scans installed skills and MCP servers together. Highest recall on skillscan.sh's benchmark among tools tested. |
| [SkillSpector](https://github.com/NVIDIA/skillspector) (NVIDIA) | Static + optional LLM | Yes | Yes | Optional | Documents its own scope limits: non-English, images, runtime. |
| Gen Agent Trust Hub | Cloud | No | No | Yes | One of three auditors on skills.sh. |
| Socket | Supply chain | No | No | Partial | One of three auditors on skills.sh. Flags unpinned remote installs aggressively. |
| VirusTotal Code Insight | Cloud | No | No | Yes | Used by ClawHub for new publications after ClawHavoc. |
| Enkrypt Skill Scanner, JFrog, Superagent | Commercial | No | Varies | Yes | API or platform products; no public corpus. |
| `skillscan` (PyPI) | Static CLI | Yes | Yes | No | Unrelated to this site. |

## What we have observed running Cisco's scanner on 618 skills

- Signature rules produce most CRITICAL findings and most false positives. The worst cases are security tools and test corpora that contain attack strings as data.
- The LLM layer produces fewer, better findings, with readable remediation text. Its meta-validation confirmed about 60 percent at high confidence and downgraded most of the rest for context.
- Running without the LLM layer, as community scans do, roughly halves the useful findings and leaves only signature hits.
- Scanner version matters. We pin it and record it per run, because rule updates change results on unchanged skills.

## Known bypasses

Trail of Bits (June 2026) bypassed every scanner on this list that they tested, including the one we run, using whitespace padding, bytecode, archive indirection, and persuasive framing. The Cloud Security Alliance's follow-up notes document further evasions of ClawHub's VirusTotal integration between February and May 2026. No scanner here should be treated as a gate. See [what scanners catch and miss](/learn/what-scanners-catch-and-miss/).

## Adding scanners to this corpus

Running a second scanner over the same 618 skills, with results side by side on each skill page, is on the roadmap. It would be the first public cross-scanner dataset on real registry content. If you maintain a scanner and want it included, open an issue.

Vendor comparisons we reviewed while preparing this page were mostly written by competing vendors. We have tried to limit this page to scope and observed behaviour and to leave scoring to the benchmark.
