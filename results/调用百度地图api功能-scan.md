# Agent Skill Security Scan Report

**Skill:** baidu-map
**Directory:** ./skills/clawhub-baidu-map-api
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.48s
**Timestamp:** 2026-02-03T16:08:14.035453

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 0
- **Medium:** 0
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:17

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export BAIDU_MAP_AK="你的百度地图Access Key

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Skill description is too short

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** TRIGGER_DESCRIPTION_TOO_SHORT
**Location:** SKILL.md

**Description:** Description has only 0 words. Short descriptions may not provide enough context for the agent to determine when this skill should be used.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
