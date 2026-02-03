# Agent Skill Security Scan Report

**Skill:** insecure-defaults
**Directory:** ./skills/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.29s
**Timestamp:** 2026-02-03T14:13:15.727818

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Database connection string with embedded credentials

**Severity:** HIGH
**Category:** hardcoded_secrets
**Rule ID:** SECRET_CONNECTION_STRING
**Location:** references/examples.md:106

**Description:** Pattern detected: postgresql://admin:password@

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
