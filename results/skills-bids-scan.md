# Scan: bids

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:39.098056+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/update_schema.py:35 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/update_schema.py:36 |
