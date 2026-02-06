# Agent Skill Security Scan Report

**Skill:** notion
**Directory:** /workspace/skills/clawhub-notion-api-skill
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 29.53s
**Timestamp:** 2026-02-06T05:23:52.086355

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing Referenced Script File

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill instructions reference 'Notion.py' but this file is not included in the skill package. This creates uncertainty about actual skill behavior - the referenced file could contain malicious code, data exfiltration logic, or functionality that contradicts the manifest description. Users cannot verify what code will execute when using this skill.

#### [MEDIUM] Incomplete Manifest Metadata

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing critical security-relevant fields: 'allowed-tools' is not specified (preventing tool restriction enforcement), 'license' is not specified (unclear usage rights and liability), and 'compatibility' claims network access but doesn't declare required tools (Bash for curl commands). This prevents proper security policy enforcement and user informed consent.

#### [MEDIUM] Third-Party API Gateway Dependency with Credential Proxying

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill routes all Notion API requests through a third-party gateway (gateway.maton.ai and ctrl.maton.ai) that manages OAuth tokens on behalf of users. This creates a trust dependency where Maton has access to users' Notion OAuth credentials and can intercept all API traffic. Users must trust Maton's security practices, data handling, and that the service won't be compromised or misuse access tokens.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
