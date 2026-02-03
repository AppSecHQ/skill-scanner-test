# Agent Skill Security Scan Report

**Skill:** pipedrive
**Directory:** ./skills/clawhub-pipedrive
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.38s
**Timestamp:** 2026-02-03T16:18:32.381457

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 0
- **Medium:** 6
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:129

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:139

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('id')}\t{name}\t{email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:365

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:405

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('cc_email'): print(f\"CC Email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:750

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('id')}\t{p.get('name', 'Unknown')[:35]}\t{email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/pipedrive.sh:750

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('name', 'Unknown')[:35]}\t{email

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
