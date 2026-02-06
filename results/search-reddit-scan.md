# Agent Skill Security Scan Report

**Skill:** search-reddit
**Directory:** /workspace/skills/clawhub-search-reddit
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.50s
**Timestamp:** 2026-02-06T07:36:24.511708

## Summary

- **Total Findings:** 2
- **Critical:** 1
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
**Location:** SKILL.md:15

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export OPENAI_API_KEY="sk-YOUR-KEY

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
