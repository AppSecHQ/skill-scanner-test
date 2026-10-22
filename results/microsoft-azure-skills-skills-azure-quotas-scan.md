# Scan: azure-quotas

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 1
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:04.194335+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | scripts/check-quota.sh:67 |
