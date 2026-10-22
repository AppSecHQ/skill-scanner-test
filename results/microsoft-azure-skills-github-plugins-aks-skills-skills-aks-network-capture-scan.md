# Scan: aks-network-capture

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 1
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:48.832812+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | command_injection | Remote fetch followed by execution | scripts/generate-test-traffic.sh:149 |
