# Agent Skill Security Scan Report

**Skill:** semgrep-rule-creator
**Directory:** ./skills/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.38s
**Timestamp:** 2026-02-03T14:12:57.853645

## Summary

- **Total Findings:** 6
- **Critical:** 0
- **High:** 0
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:90

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): eval(user_input)

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:90

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): eval("safe_literal")

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:61

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:66

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:61

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): system("rm " + $

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
