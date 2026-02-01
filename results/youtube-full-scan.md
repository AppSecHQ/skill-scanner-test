# Agent Skill Security Scan Report

**Skill:** youtube-full
**Directory:** ./skills/clawhub-youtube-full
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 21.92s
**Timestamp:** 2026-02-01T07:11:55.147527

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 0
- **Medium:** 1
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

#### [MEDIUM] Hardcoded API Key Exposure Risk in Documentation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill instructions demonstrate storing the API key in shell configuration files (~/.zshenv) using echo commands. While this is a common practice, the instructions don't warn users about the security implications of storing credentials in plaintext shell configuration files that may be readable by other processes or accidentally committed to version control.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Optional Metadata Fields

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing optional but recommended fields: 'license', 'compatibility', and 'allowed-tools'. While these fields are not required per the agent skills specification, their absence makes it harder for users to understand the skill's requirements and restrictions.

#### [LOW] External API Dependency Without Rate Limiting Guidance

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill relies on an external third-party API (transcriptapi.com) with a credit-based system, but doesn't provide guidance on rate limiting, error handling, or what happens when credits are exhausted. Users could inadvertently exhaust their API credits without proper warnings.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
