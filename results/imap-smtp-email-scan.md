# Agent Skill Security Scan Report

**Skill:** imap-smtp-email
**Directory:** /workspace/skills/clawhub-imap-smtp-email
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 29.08s
**Timestamp:** 2026-02-06T03:23:02.111893

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Credential Storage in Plain Text .env File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** setup.sh

**Description:** The skill instructs users to store email credentials (IMAP_PASS, SMTP_PASS) in a plain text .env file without encryption or secure storage mechanisms. Email credentials provide full access to user's email account, enabling reading all messages, sending emails on behalf of the user, and potentially accessing sensitive personal/business information. The setup.sh script actively prompts users to enter passwords which are then written to disk in plain text.

### MEDIUM Severity

#### [MEDIUM] Missing allowed-tools Declaration

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill does not declare allowed-tools in its YAML manifest, making it unclear what agent capabilities are required. Given that the skill executes Node.js scripts (node scripts/imap.js), it requires Bash tool access at minimum. The absence of this declaration reduces transparency about the skill's execution requirements and potential security boundaries.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
