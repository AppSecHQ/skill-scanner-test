# Scan: geomaster

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:11.900342+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/data-sources.md:106 |
| MEDIUM | command_injection | Python code block executes shell commands | references/gis-software.md:262 |
| HIGH | command_injection | Python code block uses eval/exec | references/machine-learning.md:154 |
