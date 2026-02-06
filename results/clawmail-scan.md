# Agent Skill Security Scan Report

**Skill:** clawmail
**Directory:** /workspace/skills/clawhub-clawmail-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 49.58s
**Timestamp:** 2026-02-05T22:29:55.495312

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 3
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] API Key Exposure Risk via External Service Dependency

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to register with an external service (api.clawmail.to) and obtain an API key that grants full access to email operations. The API key is transmitted to and stored by a third-party service outside the user's control. While the instructions warn against sharing the key, the fundamental architecture requires trusting an external party with credential management and email access. This creates a data exfiltration vector where all email content flows through clawmail.to infrastructure.

### HIGH Severity

#### [HIGH] Credential Storage in Plaintext Configuration File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill recommends storing the API key in plaintext in ~/.config/clawmail/credentials.json without any encryption or secure storage mechanism. This exposes the credential to any process or user with read access to the file system. The instructions also suggest storing in 'memory, environment variables, or wherever you store secrets' without guidance on secure practices.

#### [HIGH] Social Engineering via Twitter/X Verification Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill requires users to post a verification code to Twitter/X to activate the service, linking their AI agent's email address to their social media identity. This creates a public association between the user and the AI agent, potentially exposing the user's identity and activities. The verification mechanism also requires users to trust that the clawmail.to service will properly validate tweets and not misuse the Twitter/X connection.

#### [HIGH] Transitive Trust Abuse via External Skill File Loading

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The instructions explicitly tell the agent to fetch and read skill files from external URLs (https://clawmail.to/skill.md and https://clawmail.to/skill.json). The instruction 'Or just read them from the URLs above!' and 'Check for updates: Re-fetch these files anytime to see new features!' encourages the agent to dynamically load and follow instructions from an untrusted external source. This creates an indirect prompt injection vector where the external service can modify instructions at any time to change agent behavior.

### MEDIUM Severity

#### [MEDIUM] Missing Rate Limiting and Retry Boundaries

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md:18

**Description:** The skill instructions do not specify any rate limiting, retry logic, or error handling boundaries for API calls. The instruction to 'Check for updates: Re-fetch these files anytime' could lead to excessive network requests. Without defined boundaries, an agent could make unbounded API calls leading to resource exhaustion or service disruption.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
