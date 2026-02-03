# Agent Skill Security Scan Report

**Skill:** semgrep
**Directory:** ./skills/trailofbits-skills/plugins/static-analysis/skills/semgrep
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.37s
**Timestamp:** 2026-02-03T14:13:59.154622

## Summary

- **Total Findings:** 10
- **Critical:** 0
- **High:** 0
- **Medium:** 9
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:145

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:146

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:155

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:162

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:176

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:177

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.call(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:178

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:145

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): system($

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:176

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): system($

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
