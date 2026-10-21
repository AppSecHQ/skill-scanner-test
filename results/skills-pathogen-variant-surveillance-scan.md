# Scan: pathogen-variant-surveillance

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 6
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:38.835197+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/lapis_client.py:173 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/lapis_client.py:178 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/lapis_client.py:313 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/lapis_client.py:315 |
