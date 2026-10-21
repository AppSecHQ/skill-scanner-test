# Scan: pi-agent

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:52.056175+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/overview.md:1 |
| CRITICAL | prompt_injection | PROMPT INJECTION detected by YARA | references/sdk.md:138 |
