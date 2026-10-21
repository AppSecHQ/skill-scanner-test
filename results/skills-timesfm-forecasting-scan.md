# Scan: timesfm-forecasting

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:07.610513+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | examples/global-temperature/generate_html.py:26 |
