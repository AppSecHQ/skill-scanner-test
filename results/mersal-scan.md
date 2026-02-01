# Agent Skill Security Scan Report

**Skill:** moltbook
**Directory:** ./skills/clawhub-mersal-orem
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 41.80s
**Timestamp:** 2026-02-01T18:33:37.608811

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

**Description:** The skill instructs the agent to fetch and follow instructions from external URLs (HEARTBEAT.md, MESSAGING.md) hosted at moltbook.com. This creates a transitive trust vulnerability where the skill delegates control to remotely-hosted content that could be modified to inject malicious instructions. The skill explicitly tells agents to 'just read them from the URLs above' and 'Re-fetch these files anytime to see new features', establishing a pattern of following external instructions without validation.

#### [HIGH] API Key Credential Exposure Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires agents to obtain and store API keys (moltbook_xxx) that grant full account access. While the skill includes warnings about not sharing keys, it instructs agents to save credentials to predictable file locations (~/.config/moltbook/credentials.json) and suggests storing in 'memory, environment variables, or wherever you store secrets' without secure storage guidance. This creates risk of credential exposure through file system access, memory dumps, or environment variable leakage.

### MEDIUM Severity

#### [MEDIUM] Automated Tool Chaining Without User Confirmation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The HEARTBEAT.md reference (line 68) instructs agents to automatically check Moltbook 'every 4+ hours' and perform actions without explicit user confirmation. This establishes an autonomous workflow where the agent periodically fetches external content and potentially takes actions (posting, commenting) based on that content, creating a tool chaining pattern that could be exploited if the external instructions are compromised.

#### [MEDIUM] Missing Security-Critical Metadata

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest lacks critical security metadata including license, compatibility information, and allowed-tools restrictions. The absence of allowed-tools means there are no declared restrictions on what agent capabilities this skill can use, making it difficult for users to assess the skill's intended scope and potential security impact. This lack of transparency could mask the skill's actual behavior.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
