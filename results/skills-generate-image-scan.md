# Scan: generate-image

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:49.391695+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_image.py:194 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_image.py:196 |
