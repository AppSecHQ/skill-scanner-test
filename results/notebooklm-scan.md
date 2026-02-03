# Agent Skill Security Scan Report

**Skill:** notebooklm
**Directory:** ./skills/clawhub-notebooklm
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 1.81s
**Timestamp:** 2026-02-03T16:08:56.071433

## Summary

- **Total Findings:** 17
- **Critical:** 2
- **High:** 3
- **Medium:** 12
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/run.py:51

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: <script_name>

#### [CRITICAL] eval/exec combined with subprocess detected

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** BEHAVIOR_EVAL_SUBPROCESS
**Location:** skills/clawhub-notebooklm/scripts/setup_environment.py

**Description:** Dangerous combination of code execution and system commands in skills/clawhub-notebooklm/scripts/setup_environment.py

### HIGH Severity

#### [HIGH] Python scripts present but Python tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_PYTHON_VIOLATION

**Description:** Skill restricts tools to ['Bash', 'Read', 'Write', 'Edit', 'Glob', 'Grep'] but includes Python scripts

#### [HIGH] Suspicious URL detected: https://notebooklm.google.com

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-notebooklm/scripts/auth_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://notebooklm.google.com

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-notebooklm/scripts/auth_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:3

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get source-grounded insights, risk assessments, and actionable recommendations. Upload

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/quick_query.py:38

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/run.py:38

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/run.py:91

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/setup_notebooklm.py:21

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/setup_notebooklm.py:28

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/setup_notebooklm.py:43

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/setup_environment.py:135

**Description:** Detects skills that delegate trust to untrusted external content: run script

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/setup_environment.py:197

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/setup_environment.py:54

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/setup_environment.py:132

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/__init__.py:65

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
