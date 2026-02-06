# Agent Skill Security Scan Report

**Skill:** security-auditor
**Directory:** /workspace/skills/clawhub-security-auditor
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.21s
**Timestamp:** 2026-02-06T07:36:32.995639

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
**Location:** SKILL.md:196

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:94

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec(`ls ${userInput}`)

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:94

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec(`ls ${

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
