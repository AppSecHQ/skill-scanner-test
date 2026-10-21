# Scan: glycoengineering

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:22.667221+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/glycan_databases.md:63 |
| MEDIUM | command_injection | Python code block executes shell commands | references/glycoshield.md:98 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/glytoucan_lookup.py:20 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/glytoucan_lookup.py:34 |
