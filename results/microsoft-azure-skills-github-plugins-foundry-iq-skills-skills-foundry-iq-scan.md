# Scan: foundry-iq

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:53.935653+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | helpers/_document_adapters.py:23 |
