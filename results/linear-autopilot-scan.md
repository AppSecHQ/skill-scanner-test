# Agent Skill Security Scan Report

**Skill:** linear-autopilot
**Directory:** /workspace/skills/clawhub-linear-autopilot
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 44.74s
**Timestamp:** 2026-02-06T04:04:43.341864

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Tool Chaining for Automated Data Flow Without User Confirmation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill implements an automated pipeline (Linear → Webhook → Discord → Clawdbot → Git) that chains multiple operations without explicit user confirmation at each step. Tasks created in Linear automatically trigger processing, status updates, and git commits. The 'autoPush: true' configuration in linear-config.json enables automatic git commits and pushes without user review, potentially exposing sensitive task data or committing unintended changes.

#### [MEDIUM] Potential Credential Exposure via Linear API Key Storage

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill stores the Linear API key in plaintext in ~/.clawdbot/linear.env file. While this is a local file with presumably restricted permissions, plaintext credential storage increases risk of exposure through backup systems, log files, or if the file permissions are misconfigured. The setup instructions don't mention setting appropriate file permissions (chmod 600).

#### [MEDIUM] Command Injection Risk in GraphQL Query Construction

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/linear-api.sh

**Description:** The linear-api.sh script constructs GraphQL queries by directly interpolating variables into query strings without proper escaping or validation. The 'graphql()' function uses string interpolation for query construction, which could allow command injection if task IDs or other parameters contain malicious input (e.g., quotes, escape sequences, or GraphQL injection payloads).

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
