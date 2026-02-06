# Agent Skill Security Scan Report

**Skill:** gold_price_mcp
**Directory:** /workspace/skills/clawhub-gold-price-mcp
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.13s
**Timestamp:** 2026-02-06T02:31:02.161605

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing Critical Manifest Metadata

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md:1

**Description:** The skill lacks essential manifest fields including 'license', 'compatibility', and 'allowed-tools'. While 'allowed-tools' is optional, its absence makes it impossible to verify if the skill's behavior (making network requests, executing Python) aligns with intended restrictions. The missing compatibility field obscures that this skill requires network access and Python 3.10, which may not work in all environments claimed by default.

#### [MEDIUM] External Network Dependency Without Disclosure

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** gold-price-mcp.py:23

**Description:** The skill makes HTTP requests to an external API (api.chnwt.dev) without clearly disclosing this network dependency in the manifest. While the API appears legitimate (Thai gold price data), users cannot assess the privacy implications or network requirements before installation. The domain 'chnwt.dev' is not a well-known official Thai government domain, raising questions about data provenance.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
