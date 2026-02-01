# Agent Skill Security Scan Report

**Skill:** birthday-reminder
**Directory:** ~/skill-scanner-test/skills/clawhub-birthday-reminder
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 1.75s
**Timestamp:** 2026-01-31T17:33:20.702924

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

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
- trigger_analyzer
