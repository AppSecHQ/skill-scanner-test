# Agent Skill Security Scan Report

**Skill:** clawbrowser
**Directory:** /workspace/skills/clawhub-clawbrowser
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 23.53s
**Timestamp:** 2026-02-05T21:55:22.334773

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Overly Permissive Bash Tool Restriction with Wildcard Pattern

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill declares 'allowed-tools: Bash(playwright-cli:*)' which uses a wildcard pattern that permits execution of ANY command starting with 'playwright-cli'. This overly broad restriction could allow unintended command execution if the playwright-cli tool has undocumented or dangerous subcommands, or if command injection vulnerabilities exist in the CLI itself. The wildcard pattern defeats the purpose of tool restrictions by not limiting to specific safe subcommands.

#### [MEDIUM] Credential Exposure Risk in Example Code

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The instruction body contains example code that demonstrates filling login credentials directly into form fields ('playwright-cli fill e2 "supersecret"'). While this is示例代码, it trains the agent to handle credentials in plaintext command-line arguments, which may be logged in shell history, process listings, or session recordings. This pattern could lead to credential exposure if users follow the example with real credentials.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
