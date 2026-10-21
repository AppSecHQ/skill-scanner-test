# Scan: waypoint-bio

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:52.489400+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | command_injection | Python code block uses eval/exec | references/python-api.md:137 |
| MEDIUM | command_injection | Python code block executes shell commands | references/python-api.md:228 |
