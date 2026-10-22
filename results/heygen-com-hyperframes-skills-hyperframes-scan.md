# Scan: hyperframes

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 15
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:34.049803+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/bake-basemap.mjs:26 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/bake-basemap.mjs:127 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/bake-basemap.mjs:128 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/bake-basemap.mjs:149 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/bake-basemap.mjs:196 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/bake-basemap.mjs:280 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/lib/main-module.test.mjs:4 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/lib/main-module.test.mjs:18 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/locate.mjs:23 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/locate.mjs:215 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/plugin-cli.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/plugin-cli.mjs:78 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/plugin-cli.test.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/plugin-cli.test.mjs:108 |
