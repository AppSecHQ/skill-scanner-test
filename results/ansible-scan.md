# Agent Skill Security Scan Report

**Skill:** ansible
**Directory:** ./skills/clawhub-ansible-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.63s
**Timestamp:** 2026-02-03T16:08:48.060771

## Summary

- **Total Findings:** 2
- **Critical:** 1
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Private key block detected

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** SECRET_PRIVATE_KEY
**Location:** SKILL.md:261

**Description:** Pattern detected: -----BEGIN OPENSSH PRIVATE KEY-----

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
