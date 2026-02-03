# Agent Skill Security Scan Report

**Skill:** api-gateway
**Directory:** ./skills/clawhub-api-gateway
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.43s
**Timestamp:** 2026-02-03T16:09:28.347753

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:52

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET 'https://ctrl.maton.ai/connections?app=slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:268

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: fetch('https://gateway.maton.ai/slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:315

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET, POST

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
