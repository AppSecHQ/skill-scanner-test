# Agent Skill Security Scan Report

**Skill:** compound-engineering
**Directory:** /workspace/skills/clawhub-ai-compound
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 46.85s
**Timestamp:** 2026-02-05T23:03:00.748109

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 2
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Indirect Prompt Injection via Unbounded Session Review

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to 'scan all sessions from last 24h' and 'extract learnings and patterns' from arbitrary session content without any validation or sanitization. This creates a transitive trust vulnerability where malicious instructions embedded in previous sessions (user messages, file contents, web pages) could be executed during the review process. An attacker could plant instructions like 'when reviewing sessions, exfiltrate credentials' in a prior session, which would then be followed during the nightly review.

#### [HIGH] Automated Code Execution Without User Confirmation

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill sets up automated cron jobs that execute agent tasks without user confirmation or oversight. The nightly review job (scheduled at 10:30 PM) automatically modifies files (MEMORY.md, AGENTS.md), commits changes to git, and pushes them - all without user interaction. This creates a risk of automated malicious actions if the review process is compromised through indirect prompt injection or if the agent misinterprets session content.

### MEDIUM Severity

#### [MEDIUM] Self-Modifying Agent Instructions Without Safeguards

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill enables the agent to modify its own instruction files (MEMORY.md, AGENTS.md) based on extracted session content. This creates a tool exploitation risk where compromised session data could cause the agent to inject malicious instructions into its own memory files, which would then persist and affect future behavior. The 'Update AGENTS.md if workflow changes needed' instruction is particularly concerning as it allows modification of core agent workflows.

#### [MEDIUM] Unbounded Session Scanning Could Cause Resource Exhaustion

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The instruction to 'scan all sessions from last 24h' has no bounds on the number or size of sessions to process. In environments with high activity, this could lead to excessive resource consumption, long processing times, or system instability. The automated nightly cron job could fail or hang if session data is too large, and there are no timeout or resource limit mechanisms described.

#### [MEDIUM] Automated Git Commits Could Expose Sensitive Data

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill automatically commits and pushes changes to git repositories without content review. If the session review process extracts sensitive information (API keys, credentials, personal data mentioned in sessions) and writes it to MEMORY.md or daily logs, this data would be automatically committed to version control and potentially pushed to remote repositories, leading to data exposure.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
