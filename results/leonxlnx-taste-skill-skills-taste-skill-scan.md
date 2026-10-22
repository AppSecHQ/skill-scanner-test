# Scan: design-taste-frontend

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 39
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:26.075462+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/assets.mjs:187 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/assets.mjs:248 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/assets.mjs:433 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/assets.mjs:570 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/assets.mjs:742 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/assets.mjs:784 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/assets.mjs:805 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/inspect.mjs:53 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:108 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:124 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:125 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:129 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:133 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:136 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:140 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:141 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:143 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:145 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:147 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:149 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:150 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:151 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:154 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:170 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:177 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/inspect.mjs:243 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/lib/cdp.mjs:4 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/lib/cdp.mjs:85 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/lib/cdp.mjs:204 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:55 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:70 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:72 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:82 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:94 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:96 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:99 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:112 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/scenes.mjs:114 |
