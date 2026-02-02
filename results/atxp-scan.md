# Agent Skill Security Scan Report

**Skill:** atxp
**Directory:** ./skills/atxp-dev-cli/skills/atxp
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.34s
**Timestamp:** 2026-02-02T02:57:07.080367

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
**Location:** SKILL.md:43

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get the messageId from `email

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
