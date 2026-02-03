# Agent Skill Security Scan Report

**Skill:** moltbot-best-practices
**Directory:** ./skills/clawhub-moltbot-best-practices
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.34s
**Timestamp:** 2026-02-03T15:54:29.221849

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:14

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get OK → then post

#### [MEDIUM] AUTONOMY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** autonomy_abuse
**Rule ID:** YARA_autonomy_abuse
**Location:** SKILL.md:41

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
