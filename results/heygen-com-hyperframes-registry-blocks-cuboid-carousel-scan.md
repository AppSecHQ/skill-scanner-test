# Scan: cuboid-carousel

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:27.738103+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/gsap-3.14.2.min.js:2096 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | assets/three.core.min.js:13955 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | assets/three.core.min.js:15734 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | assets/three.core.min.js:15767 |
| MEDIUM | obfuscation | File extension does not match actual content type | assets/three.module.min.js |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | assets/three.module.min.js:1992 |
