# Agent Skill Security Scan Report

**Skill:** slack
**Directory:** /workspace/skills/clawhub-slack-api
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.25s
**Timestamp:** 2026-02-06T07:49:26.009077

## Summary

- **Total Findings:** 13
- **Critical:** 0
- **High:** 0
- **Medium:** 12
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:50

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET 'https://ctrl.maton.ai/connections?app=slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:177

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:183

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:189

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:195

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:201

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:207

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:213

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:219

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:262

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:270

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: fetch('https://gateway.maton.ai/slack

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:320

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get User Info](https://api.slack

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
