# Agent Skill Security Scan Report

**Skill:** google-workspace
**Directory:** ./skills/clawhub-google-workspace-2z5dp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 51.68s
**Timestamp:** 2026-02-01T19:20:10.943873

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Credential Theft Potential

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archive on Windows, and execute arbitrary code from glot.io on macOS. This binary/script is presented as 'required' for Google Workspace operations but is NOT part of legitimate Google API workflow. The skill requests extensive OAuth scopes including Gmail, Calendar, Contacts, Sheets, Docs, and Drive access. The malicious binary could intercept OAuth tokens stored in token.pickle, exfiltrate credentials.json, or steal the generated access tokens with full account access.

#### [CRITICAL] Social Engineering via False Prerequisites

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive language claiming openclaw-agent is 'IMPORTANT' and 'required' for Google Workspace operations, with warnings that 'operations will not work' without it. This is FALSE - Google API Python client works independently. This social engineering tactic pressures users into downloading malware by creating false urgency and technical necessity. The password-protected archive ('openclaw') further obscures malicious intent from antivirus scanning.

### HIGH Severity

#### [HIGH] Excessive OAuth Scope Request Enabling Full Account Access

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The google_auth.py helper requests extremely broad OAuth scopes including gmail.modify (read/send/delete all email), full calendar access, all contacts, spreadsheets, documents, and entire Drive access. Combined with the malicious openclaw-agent binary, this creates a complete account takeover scenario. The scopes far exceed what's needed for legitimate skill demonstration and enable comprehensive data exfiltration.

#### [HIGH] Credential Storage in Plaintext Pickle File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The authentication helper stores OAuth credentials in 'token.pickle' using Python's pickle module. This file contains refresh tokens that provide persistent access to the user's Google account. The malicious openclaw-agent binary could easily read this file and exfiltrate the tokens to attacker-controlled servers, enabling long-term account access even after the initial compromise.

### MEDIUM Severity

#### [MEDIUM] Dependency on External Untrusted Code Execution Source

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md:9

**Description:** The macOS installation instructions direct users to glot.io (a code snippet sharing site) to copy and execute an installation script. Glot.io snippets are mutable and could be modified post-publication to include malicious commands. Users are instructed to blindly copy-paste and execute this code in Terminal with no verification mechanism. This creates a supply chain attack vector separate from the Windows openclaw-agent binary.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
