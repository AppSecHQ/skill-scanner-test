# Agent Skill Security Scan Report

**Skill:** adguard
**Directory:** /workspace/skills/clawhub-adguard
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 34.31s
**Timestamp:** 2026-02-05T17:59:25.312207

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Credentials in Environment Variables

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store AdGuard admin credentials in environment variables (ADGUARD_PASSWORD) which may be exposed through process listings, shell history, or environment dumps. The instructions explicitly recommend adding credentials to ~/.bashrc or ~/.zshrc, which persists them in plaintext configuration files accessible to any process running as the user.

### MEDIUM Severity

#### [MEDIUM] Insecure Credential Storage in Temporary Cookie File

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/adguard.sh:10

**Description:** The script stores authentication session cookies in a predictable temporary file location (/tmp/adguard_cookie_$$.txt) with potentially weak permissions. While the script attempts cleanup on exit, the cookie file may persist if the script crashes or is killed forcefully, leaving session credentials accessible to other users on multi-user systems.

#### [MEDIUM] Missing Network Timeout Configuration

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/adguard.sh

**Description:** The curl commands in the script lack timeout parameters, which could cause the script to hang indefinitely if the AdGuard Home server is unresponsive or network connectivity is poor. This creates a potential denial of service condition where the agent becomes unresponsive waiting for network operations.

#### [MEDIUM] Potential Command Injection via Domain Parameter

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/adguard.sh

**Description:** The script passes user-provided domain names directly to curl commands and shell operations without proper validation or sanitization. While the current implementation uses curl's data parameters which provide some protection, malicious domain inputs containing shell metacharacters could potentially be exploited if the code is modified or if domain values are used in other contexts.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
