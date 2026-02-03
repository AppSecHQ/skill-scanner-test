# Agent Skill Security Scan Report

**Skill:** firebase-apk-scanner
**Directory:** ./skills/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.42s
**Timestamp:** 2026-02-03T14:13:36.050178

## Summary

- **Total Findings:** 4
- **Critical:** 3
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Google API key detected

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** SECRET_GOOGLE_API
**Location:** references/vulnerabilities.md:22

**Description:** Pattern detected: AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#### [CRITICAL] Google API key detected

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** SECRET_GOOGLE_API
**Location:** references/vulnerabilities.md:596

**Description:** Pattern detected: AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#### [CRITICAL] Google API key detected

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** SECRET_GOOGLE_API
**Location:** references/vulnerabilities.md:742

**Description:** Pattern detected: AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q

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
