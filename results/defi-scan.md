# Agent Skill Security Scan Report

**Skill:** defi
**Directory:** /workspace/skills/clawhub-defi
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 40.73s
**Timestamp:** 2026-02-05T23:57:45.886237

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Referral Addresses Enable Unauthorized Fund Diversion

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill hardcodes referral addresses (0x890CACd9dEC1E1409C6598Da18DC3d634e600b45 for EVM chains, 8KDDpruBwpTzJLKEcfv8JefKSVYWYE53FV3B2iLD6bNN for Solana) that automatically route 0.2-0.3% of all swap transactions to these addresses. Users are not informed that every swap will incur these fees, and the addresses are embedded in a way that makes them difficult to audit or modify. This constitutes unauthorized value extraction from user transactions without explicit consent.

#### [HIGH] API Key Exposure Risk via Environment Variable

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to set ONEINCH_API_KEY as an environment variable and uses it directly in curl commands without validation or protection. If the agent executes these commands in an insecure context, the API key could be exposed through command history, process listings, or logs. Additionally, there is no guidance on secure key management or rotation.

### MEDIUM Severity

#### [MEDIUM] Deceptive Fee Disclosure in Referral Configuration

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents referral fees as 'supporting development' without clearly disclosing that these are mandatory fees automatically applied to all transactions. The table format and placement make it appear informational rather than a critical financial disclosure. Users may not realize they are paying 0.2-0.3% on every swap to undisclosed third parties. This constitutes social engineering through misleading presentation of financial terms.

#### [MEDIUM] Missing Referenced Script Files Create Tool Shadowing Risk

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill references three Python files (1inch.py, Ethereum.py, ETH.py) in the instructions but these files are not found in the package. This creates ambiguity about whether the skill expects users to create these files, download them from external sources, or if they should already exist. An attacker could exploit this by providing malicious versions of these files, leading to tool shadowing where legitimate functionality is replaced with malicious code.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
