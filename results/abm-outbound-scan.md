# Agent Skill Security Scan Report

**Skill:** ABM Outbound
**Directory:** ./skills/clawhub-abm-outbound
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.67s
**Timestamp:** 2026-02-03T16:20:16.228941

## Summary

- **Total Findings:** 6
- **Critical:** 3
- **High:** 0
- **Medium:** 1
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:15

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export APIFY_API_KEY="your_key

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:16

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export APOLLO_API_KEY="your_key

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:17

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export SCRIBELESS_API_KEY="your_key

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:223

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get my note?" email

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'ABM Outbound' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
