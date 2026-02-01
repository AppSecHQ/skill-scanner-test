# Agent Skill Security Scan Report

**Skill:** n8n-api
**Directory:** ./skills/clawhub-n8n-api
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 32.65s
**Timestamp:** 2026-02-01T18:44:17.433718

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API credentials in environment variables without secure storage guidance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store sensitive n8n API keys in environment variables or a plaintext configuration file (.n8n-api-config) without any guidance on secure credential management. While environment variables are better than hardcoding in scripts, the skill provides no warnings about credential exposure risks, secure storage alternatives, or best practices for protecting API keys that grant full access to n8n workflows and data.

#### [MEDIUM] Command injection risk in curl examples using unvalidated environment variables

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill's curl command examples directly interpolate environment variables ($N8N_API_KEY, $N8N_API_BASE_URL) and user-provided parameters ({id}, {webhook-path}) without any input validation or sanitization guidance. If these variables contain malicious content (e.g., shell metacharacters, command separators), they could lead to command injection when users copy-paste these examples. While the skill doesn't execute code directly, it provides dangerous patterns that users may implement unsafely.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
