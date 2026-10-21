# Scan: ncats-arax

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:55.114510+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | policy_violation | Skill declares no Write tool but bundled scripts write files | SKILL.md |
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/arax_client.py:615 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/arax_client.py:670 |
