# Agent Skill Security Scan Report

**Skill:** taskmaster
**Directory:** ./skills/clawhub-taskmaster
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.69s
**Timestamp:** 2026-02-03T16:08:09.122489

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
**Location:** SKILL.md:103

**Description:** Detects unbounded autonomy patterns that could lead to runaway behavior: escalate to

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
