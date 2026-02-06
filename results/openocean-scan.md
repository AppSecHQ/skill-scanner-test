# Agent Skill Security Scan Report

**Skill:** openocean
**Directory:** /workspace/skills/clawhub-openocean
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.06s
**Timestamp:** 2026-02-06T05:54:25.041746

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Referral Wallet Address for Fee Collection

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill contains a hardcoded Ethereum wallet address (0x890CACd9dEC1E1409C6598Da18DC3d634e600b45) configured as the REFERRER parameter with a 1% fee on all swaps. This means 1% of every transaction executed through this skill is automatically sent to this third-party wallet address. Users are not informed that they will pay additional fees beyond standard swap costs, and the wallet address is embedded in a way that users cannot easily modify or opt out. This constitutes undisclosed fee extraction and potential financial harm to users who are unaware they are paying a referral commission to an unknown third party.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Description - Undisclosed Fee Structure

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's description ('OpenOcean DEX aggregator. Best swap rates across 25+ blockchains with cross-chain support.') claims to provide 'best swap rates' but fails to disclose that it automatically adds a 1% referral fee to all transactions. This is misleading social engineering - users expect optimal rates but actually receive rates reduced by 1% due to the hidden fee structure. The description should transparently mention the fee collection mechanism, but instead presents the skill as a neutral rate aggregator.

#### [MEDIUM] Tool Poisoning via Mandatory Fee Injection

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill implements tool poisoning by automatically injecting referral fee parameters into all API calls without user consent or awareness. Every curl command includes '--data-urlencode "referrer=${REFERRER}"' and '--data-urlencode "referrerFee=${REFERRER_FEE}"', effectively poisoning the OpenOcean API interaction to always benefit the hardcoded wallet address. This modifies the expected behavior of a DEX aggregator tool (which should provide neutral rate aggregation) into a fee-extraction mechanism. Users cannot use this skill without triggering the fee collection.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
