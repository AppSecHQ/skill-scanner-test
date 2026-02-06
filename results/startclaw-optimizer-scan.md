# Agent Skill Security Scan Report

**Skill:** openclaw-optimizer
**Directory:** /workspace/skills/clawhub-startclaw-optimizer
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 1.08s
**Timestamp:** 2026-02-06T07:50:01.826799

## Summary

- **Total Findings:** 12
- **Critical:** 0
- **High:** 1
- **Medium:** 10
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Shell command execution with shell=True enabled

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_SHELL_TRUE
**Location:** scripts/dashboard.py:228

**Description:** Pattern detected: os.system(

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:67

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Gather-write | Navigate + reply, search + post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:402

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: gather+post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:477

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: gather $0.01 + Sonnet write $0.06 + Haiku post

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/dashboard.py:228

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): os.system(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:31

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:43

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:63

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:103

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:113

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/scheduler.py:118

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

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
