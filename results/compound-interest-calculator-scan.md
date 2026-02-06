# Agent Skill Security Scan Report

**Skill:** compound-engineering
**Directory:** /workspace/skills/clawhub-compound-calc
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 44.87s
**Timestamp:** 2026-02-05T23:07:25.098591

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 2
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Transitive Trust Abuse - Unbounded Session Content Processing

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to 'scan all sessions from last 24h' and 'extract learnings and patterns' from arbitrary session content without validation. This creates a transitive trust vulnerability where malicious instructions embedded in previous sessions (chat logs, user inputs, file contents) could be executed as trusted commands during the review process. An attacker could poison session history with prompt injection payloads that activate during nightly reviews.

#### [HIGH] Automated Tool Chaining Without User Confirmation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill creates automated workflows (cron jobs) that chain multiple sensitive operations: read sessions → extract data → modify files (MEMORY.md, AGENTS.md) → commit to git → push to remote repository. This happens automatically at 10:30 PM daily without user confirmation. An attacker who compromises session data could trigger unauthorized file modifications and code repository changes through the automated review loop.

### MEDIUM Severity

#### [MEDIUM] Unbounded Autonomy - Continuous Self-Modification Loop

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill creates a self-modifying system where the agent continuously updates its own instructions (MEMORY.md, AGENTS.md) based on extracted patterns. The instruction 'Update AGENTS.md if workflow changes needed' allows the agent to modify its own behavior autonomously. Combined with automated cron execution, this creates potential for runaway behavior, instruction drift, or accumulation of corrupted directives over time without human oversight.

#### [MEDIUM] Over-Collection of Session Data

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill collects 'all sessions from last 24h' without scope limitations or data minimization. This includes potentially sensitive information from all user interactions, file contents, API responses, and system outputs. The broad collection pattern ('extract learnings and patterns' from everything) could accumulate sensitive data (credentials, API keys, personal information) in memory files that persist and get committed to git repositories.

#### [MEDIUM] Git Command Injection Risk via Commit Messages

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs committing changes with a message pattern 'compound: daily review YYYY-MM-D' (note: message appears truncated in instructions). If the date or any extracted content is incorporated into git commit messages or commands without proper sanitization, this could enable command injection. Malicious session content could inject shell commands through git commit message formatting.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
