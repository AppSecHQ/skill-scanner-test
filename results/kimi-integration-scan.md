# Agent Skill Security Scan Report

**Skill:** kimi-integration
**Directory:** /workspace/skills/clawhub-kimi-integration
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.27s
**Timestamp:** 2026-02-06T03:47:06.013007

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Network Data Transmission to External Services

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to configure Clawdbot to send data to external third-party API endpoints (api.moonshot.cn and api.kimi.com) without adequate security warnings or data handling guidance. The configuration examples show direct integration with external services that will receive all user prompts and conversations. There is no mention of data privacy, retention policies, or what data these services collect.

### LOW Severity

#### [LOW] Missing Security Metadata in Manifest

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The YAML manifest is missing critical security-related fields including 'allowed-tools', 'license', and 'compatibility'. While 'allowed-tools' is optional per the spec, its absence means there are no declared restrictions on what agent tools this skill can use. The skill includes a bash script that makes network calls, but this capability is not declared anywhere in the manifest.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
