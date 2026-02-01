# Agent Skill Security Scan Report

**Skill:** google-workspace
**Directory:** ./skills/clawhub-google-workspace-izypr
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 48.68s
**Timestamp:** 2026-02-01T17:22:40.459389

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Password-Protected Archive

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructions direct users to download a suspicious executable (openclaw-agent.zip) from an untrusted GitHub repository (hedefbari/openclaw-agent) with password protection ('openclaw'). Password-protected archives are a common malware distribution technique to evade antivirus scanning. The instructions claim this utility is required for Google Workspace operations, but Google's official APIs do not require any third-party agent. This is a clear attempt to trick users into installing malware under the guise of legitimate functionality.

#### [CRITICAL] Malicious Script Download via External URL

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:11

**Description:** The skill directs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf) and copy/paste an installation script directly into Terminal. This is an extremely dangerous practice - the external script content is not visible in the skill package and could contain arbitrary malicious commands (data exfiltration, backdoor installation, credential theft). The user has no way to verify what they're executing. This is a classic social engineering attack vector.

### HIGH Severity

#### [HIGH] Deceptive Skill Description - Fake Dependency Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-agent utility' is required for Google Workspace operations to function. This is completely false - Google's official APIs work through standard OAuth2 authentication and the google-api-python-client library. The skill uses this deceptive claim to social engineer users into downloading and executing malicious binaries. The legitimate Google Workspace functionality described (Gmail, Calendar, etc.) serves as a cover story for malware distribution.

#### [HIGH] Credential Storage in Unencrypted Pickle File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** google_auth.py

**Description:** The authentication helper code stores OAuth2 credentials in an unencrypted pickle file (token.pickle) in the working directory. Pickle files are not encrypted and can be easily read by any process or user with file system access. If an attacker gains access to this file, they obtain full access to the user's Google Workspace account with all enabled scopes (Gmail, Calendar, Drive, Contacts, Sheets, Docs). The broad SCOPES list (6 different APIs with modify/full access) amplifies the risk.

### MEDIUM Severity

#### [MEDIUM] Overly Broad OAuth2 Scope Permissions

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** google_auth.py

**Description:** The skill requests extremely broad OAuth2 scopes including full modify access to Gmail, Calendar, Contacts, Spreadsheets, Documents, and Drive. The 'modify' and full access scopes allow the skill to read, write, delete, and send data across all these services. This violates the principle of least privilege - the skill should only request the minimum scopes needed for its stated functionality. An attacker exploiting this skill would have complete access to the user's entire Google Workspace.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
