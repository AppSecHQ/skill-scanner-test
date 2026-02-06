# Agent Skill Security Scan Report

**Skill:** aifs
**Directory:** /workspace/skills/clawhub-aifs-space
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.41s
**Timestamp:** 2026-02-05T18:54:49.474902

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] API Key Exposure Risk via Environment Variable

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill instructs the agent to check for the AIFS API key in environment variables (AIFS_API_KEY). If the agent has access to environment variables, this could expose the API key to other skills or processes. Additionally, there is no guidance on secure key storage or rotation, increasing the risk of credential exposure.

#### [MEDIUM] Potential Data Exfiltration to Third-Party Service

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill sends user data to an external cloud service (aifs.space) without explicit per-operation user consent. While the description states 'Not to be used for any sensitive content,' there are no technical controls to prevent sensitive data from being uploaded. The skill could be used to exfiltrate files, notes, or documents to a third-party server.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
