# Scan: hugging-science

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:51.497731+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| HIGH | command_injection | Active instruction acquires and executes remote content | SKILL.md:136 |
| HIGH | command_injection | Python code block uses eval/exec | references/using-models.md:42 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/fetch_catalog.py:97 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/fetch_catalog.py:99 |
