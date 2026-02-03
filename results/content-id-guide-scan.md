# Agent Skill Security Scan Report

**Skill:** Content ID Guide
**Directory:** ./skills/clawhub-content-id-guide
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.34s
**Timestamp:** 2026-02-03T16:19:25.657283

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 2
- **Info:** 0

## Findings

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'Content ID Guide' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

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
