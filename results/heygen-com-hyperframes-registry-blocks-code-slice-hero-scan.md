# Scan: code-slice-hero

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 8
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:24.901668+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/gsap-3.14.2.min.js:2096 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | shadows.js:24 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | shadows.js:35 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | shadows.js:66 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | surface.js:74 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | surface.js:84 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | surface.js:85 |
