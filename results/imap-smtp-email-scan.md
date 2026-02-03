# Agent Skill Security Scan Report

**Skill:** imap-smtp-email
**Directory:** ./skills/clawhub-imap-smtp-email
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.65s
**Timestamp:** 2026-02-03T15:58:44.707883

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
**Location:** SKILL.md:3

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read, search, and manage email via IMAP protocol. Send email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:63

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Fetch full email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** setup.sh:124

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: read -p "Email address: " EMAIL

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
