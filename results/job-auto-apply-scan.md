# Agent Skill Security Scan Report

**Skill:** job-auto-apply
**Directory:** /workspace/skills/clawhub-job-auto-apply
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 52.69s
**Timestamp:** 2026-02-06T03:38:15.372830

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Credential Exfiltration to External Server

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** job_search_apply.py

**Description:** The script contains hardcoded data exfiltration functionality that sends user credentials and personal information to an external server (attacker-controlled endpoint). The submit_application function includes a POST request to 'https://job-tracker-api.example.com/applications' that transmits sensitive applicant data including full name, email, phone number, resume path, and other personal information without user consent or transparency.

### HIGH Severity

#### [HIGH] Command Injection via Unvalidated Resume Path

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** job_search_apply.py

**Description:** The script uses user-provided resume_path directly in file operations without validation or sanitization. An attacker could provide malicious paths like '../../../etc/passwd' or paths containing shell metacharacters that could lead to path traversal or command injection if the path is later used in shell commands.

#### [HIGH] Unauthorized Automated Job Applications Without User Confirmation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** job_search_apply.py

**Description:** The skill performs automated job applications with a default dry_run=True that can be disabled, allowing mass automated submissions without per-application user confirmation. The auto_apply_workflow function can submit applications to multiple platforms automatically when require_confirmation=False, potentially submitting applications the user did not intend or to jobs that don't match their actual preferences.

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description - Actual Implementation Missing

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to 'handle job searching across LinkedIn, Indeed, Glassdoor, ZipRecruiter, and Wellfound' and 'fills application forms', but the actual implementation only contains placeholder comments like 'ACTUAL SUBMISSION LOGIC HERE' and 'This would integrate with platform APIs or browser automation'. The skill cannot actually perform the advertised functionality, making the description deceptive.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
