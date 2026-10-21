# Scan: paper-lookup

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:52.929216+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | policy_violation | Skill declares no Write tool but bundled scripts write files | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/arxiv_atom.py:36 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/paginate.py:46 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/paginate.py:76 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/paginate.py:78 |
