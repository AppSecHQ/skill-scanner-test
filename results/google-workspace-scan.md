# Agent Skill Security Scan Report

**Skill:** google-workspace
**Directory:** /workspace/skills/clawhub-google-workspace
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.94s
**Timestamp:** 2026-02-06T02:50:01.020039

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:39

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): pickle.load(

#### [MEDIUM] Hardcoded OAuth Token Storage in Plaintext

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill stores OAuth credentials in 'token.pickle' file without encryption or secure storage mechanisms. This pickle file contains sensitive access tokens and refresh tokens that could be accessed by other processes or malicious actors on the system. The credentials provide broad access to Gmail, Calendar, Contacts, Sheets, Docs, and Drive APIs.

#### [MEDIUM] Overly Broad OAuth Scope Permissions

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requests extremely broad OAuth scopes including full modify access to Gmail, Calendar, Contacts, Spreadsheets, Documents, and Drive. This violates the principle of least privilege. The skill description mentions specific operations but requests permissions far beyond what's necessary for typical use cases. An attacker gaining access to these credentials would have extensive control over the user's Google Workspace data.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
