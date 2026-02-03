# Agent Skill Security Scan Report

**Skill:** interpreting-culture-index
**Directory:** ./skills/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 2.35s
**Timestamp:** 2026-02-03T14:12:39.734340

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/culture_index/extract.py:105

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get("email

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
