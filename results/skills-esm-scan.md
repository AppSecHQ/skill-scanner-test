# Scan: esm

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:09.309343+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | command_injection | Python code block uses eval/exec | SKILL.md:109 |
| HIGH | command_injection | Python code block uses eval/exec | references/biohub-platform.md:77 |
| HIGH | command_injection | Python code block uses eval/exec | references/esm-c-api.md:15 |
| HIGH | command_injection | Python code block uses eval/exec | references/esm-c-api.md:68 |
