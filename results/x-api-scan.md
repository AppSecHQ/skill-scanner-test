# Agent Skill Security Scan Report

**Skill:** x-api
**Directory:** ./skills/clawhub-x-api
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.36s
**Timestamp:** 2026-02-03T16:16:56.486731

## Summary

- **Total Findings:** 5
- **Critical:** 4
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:29

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export X_API_KEY="your-api-key

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:30

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export X_API_SECRET="your-api-secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:31

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export X_ACCESS_TOKEN="your-access-token

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:32

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export X_ACCESS_SECRET="your-access-token-secret

### LOW Severity

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
