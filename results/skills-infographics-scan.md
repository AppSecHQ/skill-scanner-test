# Scan: infographics

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:52.093156+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 2 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 2 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/infographics/scripts/generate_infographic_ai.py |
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | social_engineering | Potential description-behavior mismatch | SKILL.md |
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_infographic_ai.py:628 |
