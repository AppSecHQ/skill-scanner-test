# Agent Skill Security Scan Report

**Skill:** crypto-gold-monitor
**Directory:** /workspace/skills/clawhub-crypto-gold-monitor
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.22s
**Timestamp:** 2026-02-06T07:56:04.133970

## Summary

- **Total Findings:** 8
- **Critical:** 7
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:13

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:14

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;36m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:15

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;35m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:17

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** crypto-monitor.sh:17

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

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
