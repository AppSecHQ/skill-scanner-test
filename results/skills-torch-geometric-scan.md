# Scan: torch-geometric

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:06.385793+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | command_injection | Python code block uses eval/exec | SKILL.md:226 |
| HIGH | command_injection | Python code block uses eval/exec | references/explainability.md:112 |
| HIGH | command_injection | Python code block uses eval/exec | references/link_prediction.md:78 |
| HIGH | command_injection | Python code block uses eval/exec | references/link_prediction.md:123 |
