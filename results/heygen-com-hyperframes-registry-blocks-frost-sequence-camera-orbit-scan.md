# Scan: frost-sequence-camera-orbit

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 13
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:31.457285+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | assets/frost.js:41 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/frost.js:398 |
| MEDIUM | obfuscation | Large hex-encoded blob (possible obfuscation) | assets/frost.js:1063 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/gsap-3.14.2.min.js:2096 |
| LOW | supply_chain_attack | Unpinned dependency | source/package.json:9 |
| LOW | supply_chain_attack | Unpinned dependency | source/package.json:10 |
| LOW | supply_chain_attack | Unpinned dependency | source/package.json:13 |
| MEDIUM | obfuscation | File extension does not match actual content type | source/src/core/clock.ts |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | source/src/shape/logo.ts:96 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | source/src/shape/text.ts:13 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | source/tools/run-shard-compile.mjs:4 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | source/tools/run-shard-compile.mjs:23 |
