# Agent Skill Security Scan Report

**Skill:** hyperliquid
**Directory:** ./skills/clawhub-hyperliquid-cli
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.47s
**Timestamp:** 2026-02-03T16:08:37.783823

## Summary

- **Total Findings:** 3
- **Critical:** 2
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
**Location:** SKILL.md:42

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: Export the private key

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:53

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export HYPERLIQUID_PRIVATE_KEY=0x...your_private_key

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
