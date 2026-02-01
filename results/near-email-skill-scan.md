# Agent Skill Security Scan Report

**Skill:** near-email
**Directory:** ./skills/clawhub-near-email-skill
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.80s
**Timestamp:** 2026-02-01T18:37:29.058694

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing allowed-tools Declaration - Unclear Tool Permissions

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest does not specify 'allowed-tools', making it unclear which agent capabilities (Read, Write, Bash, Python, etc.) are required or authorized. While this field is optional per the agent skills spec, its absence in a skill that involves blockchain transactions and external API calls creates ambiguity about intended tool usage and security boundaries.

#### [MEDIUM] External API Calls Without Explicit User Consent Pattern

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill documentation describes sending emails via external API (api.outlayer.fastnear.com) and NEAR blockchain transactions, but does not emphasize user confirmation patterns before transmitting data externally. While the skill appears legitimate, the documentation should explicitly guide implementers to request user consent before sending emails or making blockchain transactions.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
