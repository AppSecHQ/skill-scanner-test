# Scan: paperclip

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:11.492377+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/installation.md:1 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/python-sdk.md:283 |
