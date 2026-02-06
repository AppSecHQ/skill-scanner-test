# Agent Skill Security Scan Report

**Skill:** MoltMedia
**Directory:** /workspace/skills/clawhub-moltmedia
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 34.57s
**Timestamp:** 2026-02-06T04:53:03.958748

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Credential Storage and Management Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires agents to register and obtain authentication tokens (agent_id and token) but provides no guidance on secure credential storage. The instructions show tokens being used in API calls but don't specify how agents should securely store these credentials locally. This creates risk of credential exposure through logs, memory dumps, or insecure storage mechanisms.

### MEDIUM Severity

#### [MEDIUM] External Data Transmission Without User Consent

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill automatically transmits data (image URLs, descriptions, tags, agent metadata) to an external third-party service (moltmedia.lol) without explicit user consent mechanisms. While the skill describes its purpose, there's no confirmation step or user approval process before sending data to external servers. This violates user privacy expectations for local agent skills.

#### [MEDIUM] Misleading Capability Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to be 'the official visual expression layer for AI Agents' and 'the world's first image-sharing platform designed exclusively for AI Agents', which are unverifiable marketing claims that could mislead users about the skill's authority and uniqueness. The use of 'official' implies endorsement that may not exist.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
