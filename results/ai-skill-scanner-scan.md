# Agent Skill Security Scan Report

**Skill:** skill-scanner
**Directory:** ./skills/clawhub-ai-skill-scanner
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 13.91s
**Timestamp:** 2026-02-03T16:05:19.867191

## Summary

- **Total Findings:** 19
- **Critical:** 7
- **High:** 4
- **Medium:** 7
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Dangerous code execution functions that can execute arbitrary code

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_EVAL
**Location:** scripts/advanced_checks.py:337

**Description:** Pattern detected: eval(

#### [CRITICAL] Direct socket connection to external server

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SOCKET_CONNECT
**Location:** scripts/advanced_checks.py:443

**Description:** Pattern detected: socket.create_connection

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/advanced_checks.py:97

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: TEMPLATE

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/advanced_checks.py:98

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: template

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/advanced_checks.py:349

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: Function(

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/advanced_checks.py:415

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: function (

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** scripts/scan.py:131

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: socat.*exec

### HIGH Severity

#### [HIGH] Suspicious URL detected: http.client

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-ai-skill-scanner/scripts/advanced_checks.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: http.client.HTTPConnection

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-ai-skill-scanner/scripts/advanced_checks.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: http.client.HTTPSConnection

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-ai-skill-scanner/scripts/advanced_checks.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https?://([a-zA-Z0-9._-]+\.[a-zA-Z]{2,})(?:[:/]|$)

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-ai-skill-scanner/scripts/advanced_checks.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/advanced_checks.py:322

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: fetch|axios\.(?:get|post|put|delete|patch|request)|got|got\.(?:get|post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/advanced_checks.py:322

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get|post|put|delete|patch|request)|got|got\.(?:get|post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/advanced_checks.py:323

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get|post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/advanced_checks.py:458

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get", "requests.post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/scan.py:50

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: fetch|axios|got|request|http\.request|https\.request|urllib\.request|requests\.(get|post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/scan.py:51

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get|post

#### [MEDIUM] AUTONOMY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** autonomy_abuse
**Rule ID:** YARA_autonomy_abuse
**Location:** scripts/scan.py:119

**Description:** Detects unbounded autonomy patterns that could lead to runaway behavior: autorun

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
