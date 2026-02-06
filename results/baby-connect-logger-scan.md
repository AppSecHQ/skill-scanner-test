# Agent Skill Security Scan Report

**Skill:** activecampaign
**Directory:** /workspace/skills/clawhub-babyconnect
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.09s
**Timestamp:** 2026-02-05T20:14:11.528898

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Credential Storage in Plaintext Files

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store API credentials in plaintext files (~/.config/activecampaign/url and ~/.config/activecampaign/api_key) without encryption or secure storage mechanisms. While these are user-created files, the practice of storing sensitive API keys in plaintext poses a data exposure risk if the filesystem is compromised or inadvertently shared.

#### [MEDIUM] Missing Binary Dependency Without Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires an 'activecampaign' binary (specified in clawdbot.requires.bins) but provides no information about where to obtain it, how to verify its authenticity, or its provenance. Users are expected to have this binary installed, but there's no guidance on secure installation, version pinning, or integrity verification. This creates a supply chain risk where users might install malicious or compromised binaries.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
