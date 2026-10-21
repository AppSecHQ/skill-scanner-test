# Scan: nextflow

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:31.546924+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | command_injection | Remote fetch followed by execution | SKILL.md:31 |
| CRITICAL | command_injection | Remote fetch followed by execution | SKILL.md:43 |
| MEDIUM | command_injection | Remote fetch followed by execution | references/testing.md:26 |
