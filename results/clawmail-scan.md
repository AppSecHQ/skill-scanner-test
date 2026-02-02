# Agent Skill Security Scan Report

**Skill:** clawmail
**Directory:** ./skills/clawhub-clawmail-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.60s
**Timestamp:** 2026-02-02T03:06:21.185525

## Summary

- **Total Findings:** 10
- **Critical:** 4
- **High:** 0
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:121

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.clawmail.to/verify/status

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:132

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.clawmail.to/agents/YOUR_AGENT_ID

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:145

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.clawmail.to/agents/YOUR_AGENT_ID

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:314

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.clawmail.to/agents/YOUR_AGENT_ID/emails/EMAIL_ID

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:313

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get Single Email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:509

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /agents/:id/sent` | View sent email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:511

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get Email** | `GET /agents/:id/emails/:eid` | Read single email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:511

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET /agents/:id/emails/:eid` | Read single email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:512

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read single email

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
- llm_analyzer
- trigger_analyzer
- meta_analyzer
