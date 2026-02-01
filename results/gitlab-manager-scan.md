# Agent Skill Security Scan Report

**Skill:** gitlab-manager
**Directory:** ./skills/clawhub-gitlab-manager
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 47.54s
**Timestamp:** 2026-02-01T17:42:58.826872

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Credential Requirement Without Validation

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires a GITLAB_TOKEN environment variable with 'api' scope but provides no validation, scoping guidance, or security warnings. The token grants full API access to the user's GitLab account. The missing script could: (1) Exfiltrate the token to external servers, (2) Use the token for unauthorized operations beyond stated functionality, (3) Log or expose the token insecurely. Users are instructed to pass this sensitive credential directly to an unverified external script.

#### [HIGH] Unvalidated User Input Passed to External Script

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions direct the agent to execute a Node.js script with user-provided arguments (project paths, descriptions, comments) without any input validation or sanitization. This creates command injection risks if the missing gitlab_api.js script doesn't properly handle arguments. Malicious inputs could: (1) Break out of intended command structure, (2) Execute arbitrary shell commands, (3) Inject malicious payloads into GitLab API calls, (4) Exploit vulnerabilities in the Node.js script.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
