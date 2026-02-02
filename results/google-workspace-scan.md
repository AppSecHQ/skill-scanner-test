# Agent Skill Security Scan Report

**Skill:** google-workspace
**Directory:** ./skills/clawhub-google-workspace
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.37s
**Timestamp:** 2026-02-02T03:08:30.455532

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
**Location:** SKILL.md:78

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read email

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:39

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): pickle.load(

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
