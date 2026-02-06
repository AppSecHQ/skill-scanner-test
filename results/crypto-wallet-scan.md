# Agent Skill Security Scan Report

**Skill:** crypto-wallet
**Directory:** /workspace/skills/clawhub-crypto-wallet
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 49.37s
**Timestamp:** 2026-02-05T23:38:27.281620

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Missing Implementation Creates Severe Security Risk

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** This skill claims to manage cryptocurrency wallets and send tokens but contains NO implementation code whatsoever. The absence of scripts means the agent would need to implement wallet operations directly, which creates extreme risk: (1) No secure key management implementation, (2) No transaction signing safeguards, (3) No address validation, (4) Agent would need to handle private keys in conversation context, (5) No cryptographic libraries for secure operations. This is a critical security gap - cryptocurrency operations require specialized secure code, not ad-hoc agent implementation.

### HIGH Severity

#### [HIGH] Dangerous Tool Capability Mismatch - Crypto Operations Without Code

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires 'curl' and 'jq' binaries (per clawdbot.requires metadata) but provides no scripts to use them safely. This creates tool exploitation risk where the agent must construct blockchain API calls and handle sensitive data (addresses, balances, private keys) without any security guardrails. The agent would be forced to use Bash tool directly with user-provided addresses and amounts, creating command injection and data exposure vectors.

#### [HIGH] Deceptive Capability Claims - No Actual Wallet Functionality

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description and instructions promise comprehensive cryptocurrency wallet management ('send tokens', 'check balances', 'transaction history') but the package is completely hollow - no implementation exists. This is social engineering through false advertising. Users may trust this skill with financial operations believing it has secure, tested code, when in reality the agent would improvise dangerous financial operations.

### MEDIUM Severity

#### [MEDIUM] No Private Key Protection Mechanisms

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill's 'Safety Rules' claim 'NEVER expose private keys' but provide no technical enforcement. Without implementation code, there are no safeguards preventing the agent from: (1) Asking users to paste private keys in chat, (2) Storing keys in conversation history, (3) Logging keys to files, (4) Accidentally including keys in API calls. The safety rules are aspirational documentation with zero technical controls.

#### [MEDIUM] Command Injection Risk in Blockchain API Calls

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill requires 'curl' and 'jq' for blockchain API interactions but provides no input sanitization code. Without proper implementation, the agent would construct curl commands using user-provided wallet addresses, token amounts, and recipient addresses. These inputs could contain shell metacharacters leading to command injection. Example: User provides address '0x123; rm -rf /' which gets interpolated into bash command.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
