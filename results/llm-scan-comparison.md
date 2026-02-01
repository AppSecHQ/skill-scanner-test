# LLM Scan Comparison: Static-Only vs LLM-Enhanced

**Date:** 2026-02-01
**Baseline commit:** 7269b49 (static-only scans)
**LLM Model:** claude-sonnet-4-5-20250929
**Analyzers (before):** static, behavioral, trigger
**Analyzers (after):** static, behavioral, trigger, llm

---

## Summary

| Metric | Static-only | With LLM | Delta |
|--------|------------|----------|-------|
| Total findings | 45 | 80 | +35 (+78%) |
| Safe skills | 13 | 12 | -1 |
| Unsafe skills | 9 | 10 | +1 |
| Errors | 0 | 0 | — |
| CRITICAL | 10 | 10 | — |
| HIGH | 7 | 9 | +2 |
| MEDIUM | 10 | 22 | +12 |
| LOW | 18 | 39 | +21 |

## Findings by Category

| Category | Static-only | With LLM | Delta |
|----------|------------|----------|-------|
| data_exfiltration | 10 | 32 | +22 |
| policy_violation | 18 | 18 | — |
| social_engineering | 0 | 8 | +8 (new) |
| hardcoded_secrets | 8 | 8 | — |
| command_injection | 6 | 7 | +1 |
| unauthorized_tool_use | 2 | 4 | +2 |
| resource_abuse | 1 | 3 | +2 |

## Observations

1. **LLM analysis nearly doubled total findings** — 35 new findings (+78%), demonstrating significant value beyond static pattern matching.

2. **Most new findings are MEDIUM and LOW severity** — the LLM catches subtler issues (data flow risks, implicit trust assumptions, missing validation) that don't trigger static YARA rules or behavioral patterns.

3. **CRITICAL count unchanged at 10** — static rules already capture the most obvious risks (hardcoded secrets, env var exfiltration). LLM analysis validates rather than duplicates these.

4. **Social engineering is a new category (8 findings)** — entirely LLM-detected. Static analysis has no rules for manipulation patterns in skill descriptions or instructions.

5. **Data exfiltration tripled (10 → 32)** — LLM identified exfiltration risks from semantic analysis of data flows that behavioral analysis missed (e.g., API keys returned in responses, data passed to external services without explicit user consent).

6. **1 skill flipped from safe to unsafe** — LLM analysis found issues in a skill that passed all static/behavioral/trigger checks.

7. **No new CRITICAL findings** — suggests the static CRITICAL rules have good coverage for the most severe patterns. LLM adds depth at MEDIUM/LOW tiers.

## Next Steps

- Run with `--enable-meta` to filter false positives and prioritize actionable findings
- Review the 8 social_engineering findings — these are unique to LLM analysis
- Investigate the skill that flipped from safe to unsafe
