# Scan: scientific-schematics

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:08.070898+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 2 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 2 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/scientific-schematics/scripts/generate_schematic_ai.py |
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/generate_schematic_ai.py:263 |
