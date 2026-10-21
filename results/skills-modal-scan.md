# Scan: modal

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 8
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:34.822224+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | command_injection | Python code block uses eval/exec | SKILL.md:352 |
| HIGH | command_injection | Python code block uses eval/exec | references/api_reference.md:137 |
| HIGH | command_injection | Python code block uses eval/exec | references/functions.md:101 |
| MEDIUM | command_injection | Python code block executes shell commands | references/gpu.md:161 |
| MEDIUM | command_injection | Python code block executes shell commands | references/gpu.md:181 |
| MEDIUM | command_injection | Python code block executes shell commands | references/gpu.md:192 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/scheduled-jobs.md:150 |
| MEDIUM | command_injection | Python code block executes shell commands | references/web-endpoints.md:168 |
