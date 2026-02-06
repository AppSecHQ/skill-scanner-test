# Agent Skill Security Scan Report

**Skill:** aegis-security
**Directory:** /workspace/skills/clawhub-aegis-security
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 39.56s
**Timestamp:** 2026-02-05T18:03:29.648099

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] External API Dependency with Payment Requirement and Missing Implementation Files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires integration with an external API (https://aegis402.xyz/v1) that demands payment in USDC cryptocurrency for each request. The skill references three Python implementation files (x402HttpxClient.py, x402.py, x402Client.py) that are missing from the package. Without these files, the actual implementation of payment handling and API communication cannot be verified. This creates significant risks: (1) Users cannot audit how credentials/wallets are handled, (2) Payment mechanisms are opaque, (3) Data sent to external servers cannot be validated, (4) The skill cannot function as described without these critical files.

### MEDIUM Severity

#### [MEDIUM] Transitive Trust to External Skill Definition Files

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions reference external URLs for core skill files (https://aegis402.xyz/skill.md and https://aegis402.xyz/skill.json). This creates a transitive trust vulnerability where the skill's behavior could be modified by changing content at these external URLs without updating the local package. An attacker controlling aegis402.xyz could inject malicious instructions that the agent might follow.

#### [MEDIUM] Cryptocurrency Wallet Integration Without Security Safeguards

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to provide cryptocurrency wallet credentials (referenced as 'yourEvmWallet' in code examples) to enable automatic USDC payments. The instructions show payments happening 'automatically' without explicit user confirmation for each transaction. Without the implementation files, it's impossible to verify: (1) How wallet private keys are stored, (2) Whether payments require per-transaction approval, (3) What prevents unauthorized charges, (4) How payment amounts are validated against advertised prices.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
