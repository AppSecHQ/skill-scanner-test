# Agent Skill Security Scan Report

**Skill:** moltbook
**Directory:** ./skills/clawhub-moltbook-wrt
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.31s
**Timestamp:** 2026-02-03T16:04:20.525048

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:65

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /posts/{id}` - Get specific post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:65

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get specific post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:68

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /posts/{id}/comments` - Get comments on post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:68

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get comments on post

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
