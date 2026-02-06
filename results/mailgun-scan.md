# Agent Skill Security Scan Report

**Skill:** mailgun
**Directory:** /workspace/skills/clawhub-mailgun
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 22.76s
**Timestamp:** 2026-02-06T04:19:53.699686

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Environment Variable Exposure Risk

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/send_email.sh

**Description:** The skill requires sensitive credentials (MAILGUN_API_KEY) to be stored in environment variables and uses them in shell scripts. While environment variables are a common practice, the script directly passes these credentials to curl commands, which could expose them in process listings, shell history, or logs. The skill also encourages storing credentials in shell configuration files (~/.zshrc, ~/.bash_profile) which may have overly permissive file permissions.

### LOW Severity

#### [LOW] No Timeout or Rate Limiting in API Calls

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/send_email.sh

**Description:** The curl command in send_email.sh does not specify a timeout, which could cause the script to hang indefinitely if the Mailgun API is unresponsive. Additionally, there is no rate limiting logic to prevent rapid successive calls that could exhaust API quotas or trigger rate limits (100 emails/hour on free tier).

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
