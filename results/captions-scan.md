# Agent Skill Security Scan Report

**Skill:** captions
**Directory:** ./skills/clawhub-captions
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 25.96s
**Timestamp:** 2026-02-01T07:19:45.832369

## Summary

- **Total Findings:** 6
- **Critical:** 1
- **High:** 0
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:9

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export TRANSCRIPT_API_KEY

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Requirement Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store a TRANSCRIPT_API_KEY in their shell environment (~/.zshenv) but provides no validation, rotation guidance, or security warnings. Users are instructed to echo their API key directly into shell configuration files, which persists the credential in plaintext. No guidance is provided on key rotation, revocation, or secure storage alternatives.

#### [MEDIUM] External API Data Transmission Without User Consent

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill sends YouTube video URLs to an external third-party API (transcriptapi.com) without explicit user consent or privacy warnings. Video URLs may contain sensitive information (unlisted videos, private shares, watch history patterns). The skill metadata indicates env requirements but doesn't warn users that their viewing data will be transmitted to a third party.

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

**Description:** The skill manifest is missing several important metadata fields: 'license' (not specified), 'compatibility' (not specified), and 'allowed-tools' (not specified). While allowed-tools is optional, the absence of license and compatibility information makes it difficult for users to assess legal usage rights and platform compatibility. This reduces transparency about the skill's intended use cases.

#### [LOW] Referenced Files Not Found in Package

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill instructions reference two Python files (YouTube.py, video.py) that are not included in the skill package. These appear to be documentation artifacts or incomplete references. While not an active security threat, missing referenced files could indicate incomplete packaging, confuse users, or suggest removed functionality.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
