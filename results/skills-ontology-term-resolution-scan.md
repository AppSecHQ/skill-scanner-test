# Scan: ontology-term-resolution

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 8
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:42.359139+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/id_client.py:68 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/id_client.py:72 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/ols_client.py:79 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/ols_client.py:86 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/zooma_client.py:78 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/zooma_client.py:83 |
