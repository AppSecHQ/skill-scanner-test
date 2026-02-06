# Agent Skill Security Scan Report

**Skill:** qa-test-planner
**Directory:** /workspace/skills/softaworks-agent-toolkit/skills/qa-test-planner
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.21s
**Timestamp:** 2026-02-06T07:34:58.249098

## Summary

- **Total Findings:** 19
- **Critical:** 14
- **High:** 0
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:9

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:10

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:13

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;35m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:14

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;36m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/create_bug_report.sh:15

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:9

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:10

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:13

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;35m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:14

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;36m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/generate_test_cases.sh:15

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/create_bug_report.sh:32

**Description:** Pattern detected: eval "$var_name=\"$

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/create_bug_report.sh:35

**Description:** Pattern detected: eval "$

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/generate_test_cases.sh:33

**Description:** Pattern detected: eval "$var_name=\"$

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/generate_test_cases.sh:36

**Description:** Pattern detected: eval "$

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
