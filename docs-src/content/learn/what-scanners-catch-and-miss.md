---
title: "What skill scanners catch, and what they miss"
description: "An honest account of automated agent skill scanning: detection rates, the Trail of Bits bypasses, false positives, and how to use scanner output without trusting it."
slug: what-scanners-catch-and-miss
order: 3
updated: 2026-10-21
---

We run a scanner at scale and publish its output. That makes us the wrong people to oversell scanners, and the right people to say precisely where they fail.

## What they catch well

- **Known attack strings.** Reverse shells, `rm -rf /`, credential file paths, `curl | sh`. Signature rules find these reliably, which is why ClawHavoc-style campaigns that reuse a payload across hundreds of skills get caught. Our scanner [found the ClawHavoc campaign independently](/research/2026/clawhavoc-validation/) and matched Koi's C2 address.
- **Obvious exfiltration in scripts.** Data-flow analysis that follows an environment variable into a network call works when the code is plain Python or shell.
- **Clumsy prompt injection.** "Ignore previous instructions" and its relatives.
- **Hardcoded secrets.** Key-shaped strings are easy.

## What they miss

In June 2026 Trail of Bits published bypasses for Cisco skill-scanner, ClawHub's detector, and the Gen, Socket, and Snyk scanners on skills.sh. The techniques were not sophisticated:

| Technique | Why it works |
|---|---|
| Whitespace inflation (100k+ newlines) | Pushes the payload past the scanner's context or truncation limit |
| Precompiled bytecode | Signature rules read source, not `.pyc` |
| Archive or document indirection | Scanners do not expand nested containers |
| Persuasive framing | The LLM judge is a language model and can be talked into "low severity" |
| Images and non-English text | Outside the rules entirely |

The independent benchmark at [skillscan.sh](https://skillscan.sh/) reports that static scanners catch roughly 13 to 32 percent of attacks on an 84-case novel set and the best frontier models about 81 percent. The Cloud Security Alliance's research notes reach the same conclusion: no single scanner reliably detects all known classes. Academic work (CompoSkill, ColluSkill) adds a structural miss: skills that are individually clean and jointly harmful.

Our [methodology page](/methodology/) states which of these classes our pipeline mitigates. Most it does not.

## The other failure: false positives

Scanners also flag things that are fine, and at a high rate. The highest-scoring skill in our corpus by CRITICAL count is a security tool whose detection signatures ("rm -rf /", "ignore your instructions") were matched as if they were attacks. The same happens to YARA rule authoring guides, exploit-testing frameworks, and our own scanner's skill. A list of these, with reasoning, is in the [false-positive register](/research/2026/false-positive-register/).

A second-pass LLM validator reduces this. In our runs, about 60 percent of LLM findings were confirmed at high confidence and 40 percent at medium, with the medium ones usually downgraded for context the first pass missed. It does not help with signature-rule false positives, which have no second pass.

## How to use scanner output

- Treat a clean result as "nothing obvious", never as "safe".
- Treat a CRITICAL as "read this now", never as "malicious". Read the snippet. It takes thirty seconds.
- Weight findings from the LLM and behavioral layers over bare signature hits.
- Look at history. A skill that was clean and now has findings, or whose files grew tenfold, is the interesting case.
- Combine. Scanner, then the [manual checklist](/learn/how-to-audit-an-agent-skill/), then a sandbox.

The value of a scanner at scale is not the verdict on any one skill. It is consistency across thousands of skills and across time, which is what makes campaigns visible.
