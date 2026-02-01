# Agent Skill Security Scan Report

**Skill:** youtube-search
**Directory:** ./skills/clawhub-youtube-search
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.70s
**Timestamp:** 2026-02-01T07:16:07.938266

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Exposure Risk in Documentation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The SKILL.md instructions demonstrate storing the API key in ~/.zshenv using echo commands. While this is a setup instruction rather than hardcoded credentials in code, it presents a security risk by encouraging users to store sensitive credentials in shell configuration files that may be inadvertently committed to version control or exposed through other means. The skill also requires the API key to be set as an environment variable (TRANSCRIPT_API_KEY) which could be exposed through process listings or logs.

#### [MEDIUM] External API Dependency with Credential Transmission

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill makes authenticated HTTPS requests to an external third-party API (transcriptapi.com) with user credentials. While the API appears legitimate and uses HTTPS, this creates a trust dependency where user API keys are transmitted to external servers. Users must trust both the skill author's implementation and the third-party service with their credentials.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Critical Metadata Fields

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing several important metadata fields including 'license', 'compatibility', and 'allowed-tools'. While 'allowed-tools' is optional per the specification, its absence means there are no declared restrictions on what agent tools this skill can use. The missing license field makes it unclear under what terms the skill can be used or modified.

#### [LOW] Incomplete Documentation - Truncated Workflow Example

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The workflow example in the SKILL.md is truncated mid-command ('?video_url=VIDEO_ID&f'), which could lead to user confusion or incorrect implementation. While not a direct security threat, incomplete documentation could cause users to make mistakes that might have security implications.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
