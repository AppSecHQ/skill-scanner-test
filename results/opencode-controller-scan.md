# Agent Skill Security Scan Report

**Skill:** opencode-controller
**Directory:** ./skills/clawhub-opencode-controller
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.28s
**Timestamp:** 2026-02-03T16:17:00.637404

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] AUTONOMY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** autonomy_abuse
**Rule ID:** YARA_autonomy_abuse
**Location:** SKILL.md:12

**Description:** Detects unbounded autonomy patterns that could lead to runaway behavior: proceed without confirmation

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
