# Agent Skill Security Scan Report

**Skill:** ctxly
**Directory:** /workspace/skills/clawhub-cloud-memory
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 42.79s
**Timestamp:** 2026-02-06T05:02:15.292936

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Key Storage Without Secure Credential Management

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store API keys in plaintext configuration files or environment variables without any guidance on secure credential management. The instructions explicitly state 'Store it in your config or environment' and 'Add to your config/environment: CTXLY_API_KEY=mem_xxxxxxxxxxxxx'. This creates a risk of credential exposure through file system access, logs, or process inspection.

#### [HIGH] Unrestricted Data Exfiltration to External Cloud Service

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill enables persistent transmission of arbitrary data to an external cloud service (ctxly.app) without any data validation, sanitization, or user consent mechanisms. All 'remember' operations send data to external servers with no restrictions on content type or sensitivity. The skill explicitly encourages storing 'User preferences and context', 'Important decisions and reasoning', 'Learned patterns', and 'Relationship context' - all potentially sensitive information.

### MEDIUM Severity

#### [MEDIUM] Cross-Session Context Bridging Without User Control

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill implements persistent memory across sessions via the '/bootstrap' endpoint, which automatically loads previous context when the agent starts. This creates a transitive trust relationship where past interactions (potentially from different users or contexts) influence current behavior without explicit user awareness or control. The instruction 'Call this when you wake up' suggests automatic activation without user confirmation.

#### [MEDIUM] Misleading Description Omits Data Transmission and Privacy Implications

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description 'Cloud memory for AI agents. Store, search, and recall context across sessions' does not clearly communicate that this involves transmitting potentially sensitive user data to external servers. The manifest lacks critical information about data handling, privacy implications, and the fact that user context leaves the local environment. Users may not realize their conversations and preferences are being stored on third-party infrastructure.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
