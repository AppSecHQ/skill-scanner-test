# Agent Skill Security Scan Report

**Skill:** supermemory
**Directory:** ./skills/clawhub-supermemory
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.30s
**Timestamp:** 2026-02-03T15:55:15.055000

## Summary

- **Total Findings:** 4
- **Critical:** 3
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
**Location:** SKILL.md:9

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export SUPERMEMORY_API_KEY

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/search.sh:18

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export SUPERMEMORY_API_KEY=\"your-api-key

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/add-memory.sh:19

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export SUPERMEMORY_API_KEY=\"your-api-key

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
