# Agent Skill Security Scan Report

**Skill:** claude-chrome
**Directory:** /workspace/skills/clawhub-claude-chrome
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 32.38s
**Timestamp:** 2026-02-05T21:49:30.361147

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Dangerous Permission Bypass Flag Required for Operation

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:29

**Description:** The skill requires using '--dangerously-skip-permissions' flag to function in automated mode, which bypasses all security confirmations and auto-approves all actions without user consent. This flag is explicitly named 'dangerous' by the tool authors and removes critical safety guardrails that would normally require user approval for sensitive operations.

#### [HIGH] Unrestricted Browser Automation Without Scope Limits

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill provides unrestricted browser automation capabilities with no defined scope, boundaries, or safety controls. Users can execute arbitrary browser commands including navigation, form filling, clicking, and content reading across any domain without restrictions. Combined with the permission bypass flag, this creates significant tool exploitation risk.

### MEDIUM Severity

#### [MEDIUM] Potential for Credential and Sensitive Data Exposure

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill enables reading arbitrary web page content and interacting with forms without restrictions. This could be exploited to access and exfiltrate credentials, session tokens, or other sensitive data from authenticated web sessions in the user's browser. The browser has access to all cookies, local storage, and authenticated sessions.

#### [MEDIUM] Misleading Description of Security Posture

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description presents this as a simple 'alternative to OpenClaw's built-in browser tools' without disclosing the significant security implications of using '--dangerously-skip-permissions' flag or the unrestricted nature of browser automation. Users may not understand they are enabling dangerous permission bypasses.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
