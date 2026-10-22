# Scan: wizard

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:14.761735+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | template.sh:210 |
