# Scan: citation-management

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 8
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:06.211421+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 5 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 5 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/citation-management/scripts/extract_metadata.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/citation-management/scripts/search_openalex.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/citation-management/scripts/search_pubmed.py |
| MEDIUM | social_engineering | Potential description-behavior mismatch | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| MEDIUM | command_injection | Python code block executes shell commands | references/core_workflow.md:193 |
