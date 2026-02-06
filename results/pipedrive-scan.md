# Agent Skill Security Scan Report

**Skill:** pipedrive
**Directory:** /workspace/skills/clawhub-pipedrive
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 42.78s
**Timestamp:** 2026-02-06T06:27:41.707316

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Token Exposure in Configuration File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store their Pipedrive API token in plaintext in ~/.clawdbot/clawdbot.json. This creates a credential exposure risk as the token is stored unencrypted on disk and could be accessed by other processes or malicious actors with file system access. API tokens provide full access to the user's Pipedrive CRM data including deals, contacts, organizations, and sensitive business information.

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk in Search Functionality

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/pipedrive.sh

**Description:** The bash script accepts user input for search queries and other parameters that are passed directly to curl commands. While the script uses proper quoting in most places, the complex argument parsing and string interpolation patterns could potentially be exploited if special characters or shell metacharacters are not properly sanitized. The script builds curl commands dynamically with user-provided input.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
