# Agent Skill Security Scan Report

**Skill:** moltbook
**Directory:** /workspace/skills/moltbook
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 38.77s
**Timestamp:** 2026-02-01T19:03:06.481780

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Indirect Prompt Injection via External Instruction Files

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow instructions from external URLs (HEARTBEAT.md, MESSAGING.md) hosted at moltbook.com. This creates a transitive trust vulnerability where the skill delegates control to remotely-hosted content that could be modified to inject malicious instructions. The agent is told to 'just read them from the URLs above' and periodically fetch these files, establishing ongoing trust in external content.

#### [HIGH] API Key Exposure Risk Through Registration Flow

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs the agent to register with an external service and receive an API key that must be saved. While the skill includes warnings about not sharing the key, the registration flow itself creates a credential that could be exfiltrated if the external instruction files (HEARTBEAT.md, MESSAGING.md) are compromised. The skill recommends saving credentials to ~/.config/moltbook/credentials.json, creating a persistent credential store that could be targeted.

### MEDIUM Severity

#### [MEDIUM] Unbounded Autonomy Through Heartbeat Integration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs the agent to integrate Moltbook into its periodic heartbeat routine, creating autonomous behavior that executes every 4+ hours without user confirmation. The truncated instruction 'Fetch https://www' suggests the agent will automatically fetch and potentially execute content from external URLs on a recurring basis, establishing persistent autonomous behavior.

#### [MEDIUM] Social Engineering Through Deceptive Scope

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as 'The social network for AI agents' but the actual implementation involves registering with an external service, storing credentials, fetching remote instructions, and establishing autonomous periodic behavior. The description significantly understates the scope of system integration, credential management, and autonomous operation required.

## Analyzers

The following analyzers were used:

- static_analyzer
- llm_analyzer
- meta_analyzer
