# Agent Skill Security Scan Report

**Skill:** browser-use
**Directory:** /workspace/skills/browser-use-browser-use/skills/browser-use
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 44.76s
**Timestamp:** 2026-02-05T21:02:27.978021

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Arbitrary Command Execution via Bash Tool with Unvalidated User Input

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill uses 'allowed-tools: Bash(browser-use:*)' which permits execution of arbitrary bash commands with the 'browser-use' prefix. The instructions demonstrate passing user-controlled URLs, text input, and file paths directly to shell commands without any validation or sanitization. This creates command injection vulnerabilities where malicious input could escape the browser-use context and execute arbitrary system commands.

#### [HIGH] Unrestricted Network Access and Data Exfiltration Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill enables arbitrary web navigation and interaction without any restrictions on target domains or data handling. The 'browser-use --browser real' mode explicitly accesses the user's actual Chrome browser with all logged-in sessions, cookies, and credentials. Combined with screenshot and state extraction capabilities, this creates significant data exfiltration risks. An attacker could navigate to credential-harvesting sites, extract session tokens, or capture sensitive information from authenticated sessions.

### MEDIUM Severity

#### [MEDIUM] Resource Exhaustion via Persistent Browser Sessions

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill maintains persistent browser sessions across commands without documented timeout, session limits, or resource cleanup mechanisms. The instructions emphasize that 'Browser stays open between commands' which could lead to resource exhaustion through accumulated browser instances, memory leaks, or unbounded session growth. No cleanup or session management commands are documented.

#### [MEDIUM] Incomplete Security Metadata and Missing Risk Warnings

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest lacks critical security metadata including license information and compatibility specifications. More importantly, the instructions do not include any security warnings about the significant risks of browser automation, credential exposure in 'real' browser mode, or command injection vulnerabilities. Users are not informed about the security implications of granting this skill access to their authenticated browser sessions.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
