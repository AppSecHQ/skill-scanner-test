# Scan: glass-shard-title

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 6
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:24.598742+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | policy_violation | Moderate analyzability score |  |
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | policy_violation | Unanalyzable binary file | assets/ferndale_studio_01_1k.hdr |
| INFO | policy_violation | Binary file detected in skill package | assets/ferndale_studio_01_1k.hdr |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/glass-main.js:3619 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | build-bundle.mjs:8 |
