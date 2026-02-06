# Agent Skill Security Scan Report

**Skill:** llm
**Directory:** /workspace/skills/clawhub-llm
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.56s
**Timestamp:** 2026-02-06T04:12:09.354399

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing API Key Security Guidance and Potential Credential Exposure

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:1

**Description:** The skill integrates with multiple commercial LLM providers (OpenAI, Anthropic, Google) that require API keys for authentication. However, there is no documentation about secure credential management, no guidance on environment variable usage, and no warnings about API key exposure risks. Users may inadvertently expose credentials through insecure storage or logging. The skill's 'always: true' flag means it's automatically active, increasing the risk surface for credential misuse.

#### [MEDIUM] Unbounded Streaming and Resource Consumption Risk

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md:17

**Description:** The skill advertises 'streaming responses' as a feature without any documented limits, timeouts, or resource controls. Streaming from LLM providers can consume significant bandwidth and processing resources. Without proper bounds, malicious or accidental misuse could lead to excessive API costs, bandwidth exhaustion, or denial of service through unbounded streaming operations. The 'always: true' flag means this risk is present in every agent session.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
