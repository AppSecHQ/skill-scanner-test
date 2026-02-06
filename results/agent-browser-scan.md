# Agent Skill Security Scan Report

**Skill:** agent-browser
**Directory:** /workspace/skills/clawhub-agent-browser-tekken
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 25.61s
**Timestamp:** 2026-02-05T18:10:06.314402

## Summary

- **Total Findings:** 12
- **Critical:** 0
- **High:** 1
- **Medium:** 7
- **Low:** 4
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
**Location:** templates/capture-workflow.sh:7

**Description:** Pattern detected: ${1:?Usage: $0 <url> [output-dir]}

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

#### [MEDIUM] Hardcoded Credentials in Authentication Template

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** templates/authenticated-session.sh

**Description:** The authenticated-session.sh template contains placeholder credentials that could be mistakenly used with real values. The script demonstrates filling username/password fields but lacks clear warnings about credential security. While these are templates with commented examples, users might uncomment and add real credentials directly into scripts, creating a credential exposure risk.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Session State Files May Contain Sensitive Data

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** references/session-management.md

**Description:** The skill saves browser session state (cookies, localStorage, sessionStorage) to JSON files without encryption or access control warnings. While this is a legitimate feature for session persistence, saved state files may contain authentication tokens, session cookies, and other sensitive data stored in plaintext.

#### [LOW] Unbounded Loop in Proxy Rotation Example

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** references/proxy-support.md

**Description:** The proxy rotation example in references/proxy-support.md contains a while true loop without clear termination conditions or rate limiting, which could lead to resource exhaustion if the rotation logic fails.

#### [LOW] Missing allowed-tools Field in Manifest

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The YAML manifest does not include the optional 'allowed-tools' field. While this field is optional per the agent skills specification, its absence means there are no declared restrictions on which agent tools can be used. The skill declares 'allowed-tools: Bash(agent-browser:*)' which appropriately restricts to bash commands with the agent-browser prefix.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
