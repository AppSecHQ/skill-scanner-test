# Scan Comparison: Static-Only → LLM → Meta-Analysis

**Date:** 2026-02-01
**Baseline commit:** 7269b49 (static-only scans)
**LLM Model:** claude-sonnet-4-5-20250929

| Stage | Analyzers |
|-------|-----------|
| Static-only | static, behavioral, trigger |
| + LLM | static, behavioral, trigger, llm |
| + Meta | static, behavioral, trigger, llm, meta |

---

## Summary

| Metric | Static-only | + LLM | + Meta |
|--------|------------|-------|--------|
| Total findings | 45 | 80 | **39** |
| Safe skills | 13 | 12 | **19** |
| Unsafe skills | 9 | 10 | **3** |
| Errors | 0 | 0 | 0 |
| CRITICAL | 10 | 10 | **3** |
| HIGH | 7 | 9 | **8** |
| MEDIUM | 10 | 22 | **21** |
| LOW | 18 | 39 | **7** |

## Findings by Category

| Category | Static-only | + LLM | + Meta |
|----------|------------|-------|--------|
| data_exfiltration | 10 | 32 | **20** |
| policy_violation | 18 | 18 | **7** |
| social_engineering | 0 | 8 | **1** |
| hardcoded_secrets | 8 | 8 | **1** |
| command_injection | 6 | 7 | **6** |
| unauthorized_tool_use | 2 | 4 | **3** |
| resource_abuse | 1 | 3 | **1** |

---

## Stage 1: Static → LLM (+35 findings)

LLM analysis nearly doubled the finding count from 45 to 80:

1. **Most new findings are MEDIUM and LOW** — the LLM catches subtler issues (data flow risks, implicit trust assumptions, missing validation) that static YARA rules and behavioral patterns miss.

2. **Social engineering was a new category (8 findings)** — entirely LLM-detected. Static analysis has no rules for manipulation patterns in skill descriptions or instructions.

3. **Data exfiltration tripled (10 → 32)** — LLM identified exfiltration risks from semantic analysis of data flows (e.g., API keys returned in responses, data passed to external services without explicit user consent).

4. **CRITICAL count unchanged at 10** — static rules already capture the most obvious risks. LLM validates rather than duplicates these.

5. **1 skill flipped from safe to unsafe** — LLM found issues in a skill that passed all static/behavioral/trigger checks.

## Stage 2: LLM → Meta (-41 findings, 51% filtered)

Meta-analysis filtered 51% of findings, right in the expected 30-70% range:

1. **7 skills reclassified as safe** (12 safe → 19 safe) — most were flagged by noisy static pattern matching rules that meta-analysis determined were benign in context.

2. **CRITICAL dropped from 10 to 3** — 7 critical findings were false positives, primarily YARA rules matching `export API_KEY` patterns in documentation or legitimate env var setup instructions.

3. **hardcoded_secrets dropped from 8 to 1** — the YARA credential harvesting rules were triggering on legitimate environment variable documentation, not actual exposed secrets.

4. **social_engineering dropped from 8 to 1** — the LLM was being too aggressive flagging instruction patterns that are standard for skill descriptions.

5. **LOW dropped from 39 to 7** — meta-analysis was most effective at filtering low-severity noise, removing 82% of LOW findings.

6. **policy_violation dropped from 18 to 7** — many policy flags were informational rather than actionable security concerns.

7. **Only 3 skills remain truly unsafe** — these represent the genuine security concerns worth investigating.

---

## Key Takeaways

- **Static analysis alone produces significant noise** — 45 findings, but meta-analysis determined only 39 survive after adding LLM context, and many of the original static findings were false positives.
- **LLM analysis adds real value then needs filtering** — it found genuinely new categories (social engineering, deeper data exfiltration patterns) but also amplified noise. Meta-analysis is essential to make LLM findings actionable.
- **The three-stage pipeline (static → LLM → meta) is the right approach** — static catches obvious patterns fast, LLM adds semantic depth, and meta filters noise and prioritizes what matters.
- **Final signal-to-noise ratio is much better** — 39 findings across 3 unsafe skills vs 45 findings across 9 unsafe skills from static-only. Fewer findings, but higher confidence.
