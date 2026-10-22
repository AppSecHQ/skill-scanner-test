# Scan: azure-app-onboard

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 1
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:06.381891+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | command_injection | Discovery and execution chain (find -exec) | scaffold/scripts/scaffold-conformance.sh:21 |
