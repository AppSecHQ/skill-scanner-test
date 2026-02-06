# Agent Skill Security Scan Report

**Skill:** 1inch
**Directory:** /workspace/skills/clawhub-1inch
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 22.86s
**Timestamp:** 2026-02-05T17:33:33.492333

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Referral Wallet Address for Fee Collection

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill contains a hardcoded Ethereum wallet address (0x890CACd9dEC1E1409C6598Da18DC3d634e600b45) configured to receive 0.3% referral fees from all swaps. While disclosed in documentation, this creates a financial incentive structure where the skill developer profits from user transactions. Users may not realize that every swap executed through this skill automatically sends fees to this hardcoded address. This represents a form of data/value exfiltration where user transaction value is redirected to a third party.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
