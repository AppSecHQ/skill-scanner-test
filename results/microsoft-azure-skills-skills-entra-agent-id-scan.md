# Scan: entra-agent-id

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 10
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:01.031072+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | command_injection | Python code block executes shell commands | SKILL.md:126 |
| HIGH | command_injection | Active instruction invokes dynamic code or process execution | SKILL.md:136 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | SKILL.md:137 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | SKILL.md:155 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | SKILL.md:176 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | SKILL.md:221 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | SKILL.md:239 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/oauth2-token-flow.md:38 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/oauth2-token-flow.md:110 |
| MEDIUM | data_exfiltration | Python code block sends HTTP POST request | references/obo-blueprint-setup.md:62 |
