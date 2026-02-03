# Agent Skill Security Scan Report

**Skill:** test-specialist
**Directory:** ./skills/clawhub-test-specialist
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 1.90s
**Timestamp:** 2026-02-03T16:11:10.319883

## Summary

- **Total Findings:** 7
- **Critical:** 5
- **High:** 1
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_sql_injection
**Location:** SKILL.md:205

**Description:** Detects SQL injection attack patterns including keywords, tautologies, and database functions: '; DROP TABLE

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:212

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: <script>

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:212

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: </script>

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:214

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: <script>

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:1

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: # 

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/analyze_coverage.py:21

**Description:** Pattern detected: open(filepath

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
