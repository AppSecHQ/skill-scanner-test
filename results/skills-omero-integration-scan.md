# Scan: omero-integration

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 1
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:37.756403+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Direct socket connection to external server | scripts/validate_config.py:56 |
