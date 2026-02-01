# Agent Skill Security Scan Report

**Skill:** agent-browser
**Directory:** ./skills/vercel-labs-agent-browser/skills/agent-browser
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.02s
**Timestamp:** 2026-01-30T22:12:51.668476

## Summary

- **Total Findings:** 8
- **Critical:** 0
- **High:** 1
- **Medium:** 6
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Code executes bash but Bash tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_BASH_VIOLATION

**Description:** Skill restricts tools to ['Bash(agent-browser:*)'] but code executes bash commands

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/capture-workflow.sh:7

**Description:** Pattern detected: ${1:?Usage: $0 <url> [output-dir]}

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/form-automation.sh:7

**Description:** Pattern detected: ${1:?Usage: $0 <form-url>}

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/authenticated-session.sh:15

**Description:** Pattern detected: ${1:?Usage: $0 <login-url> [state-file]}

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/authenticated-session.sh:15

**Description:** Pattern detected: ${1:?Usage: $0 <login-url> [state-file]}

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/form-automation.sh:7

**Description:** Pattern detected: ${1:?Usage: $0 <form-url>}

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** templates/capture-workflow.sh:7

**Description:** Pattern detected: ${1:?Usage: $0 <url> [output-dir]}

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
- trigger_analyzer
