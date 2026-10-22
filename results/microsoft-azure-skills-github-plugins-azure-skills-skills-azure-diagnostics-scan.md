# Scan: azure-diagnostics

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:54.461936+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | scripts/test-messaging-connectivity.sh:80 |
