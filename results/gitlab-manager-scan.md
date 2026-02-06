# Agent Skill Security Scan Report

**Skill:** gitlab-manager
**Directory:** /workspace/skills/clawhub-gitlab-manager
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 24.92s
**Timestamp:** 2026-02-06T02:25:34.678904

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Credential Exposure Risk via Environment Variable

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires a GitLab Personal Access Token with 'api' scope to be set in the environment (GITLAB_TOKEN). While using environment variables for credentials is a common pattern, the skill documentation shows the token being passed directly in command examples, which could lead to credential exposure in shell history, logs, or process listings. The 'api' scope grants broad access to GitLab resources.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
