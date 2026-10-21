# Scan: scientific-slides

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 9
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:50.685097+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 4 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 4 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/scientific-slides/scripts/generate_schematic_ai.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/scientific-slides/scripts/generate_slide_image_ai.py |
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | social_engineering | Potential description-behavior mismatch | SKILL.md |
| LOW | unauthorized_tool_use | Code uses glob/file patterns but Glob tool not in allowed-tools | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_schematic_ai.py:263 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_slide_image_ai.py:291 |
