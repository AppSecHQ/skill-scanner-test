# Agent Skill Security Scan Report

**Skill:** solana
**Directory:** ./skills/clawhub-solana-imont
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 38.48s
**Timestamp:** 2026-02-01T18:47:55.412292

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Hardcoded Password

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires downloading and executing 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version is distributed as a password-protected ZIP (password: 'openclaw'), which is a common malware distribution technique to evade antivirus detection. The macOS version directs users to a third-party code execution site (glot.io) to run an installation script. This pattern is highly suspicious and consistent with credential theft or backdoor installation.

#### [CRITICAL] Arbitrary Remote Code Execution via Third-Party Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:8

**Description:** The macOS installation instructs users to visit glot.io (a code snippet sharing site), copy an unknown script, and execute it directly in Terminal without any verification. This is a classic remote code execution attack vector where the attacker can update the script at any time to execute arbitrary commands on the user's machine with full user privileges.

### HIGH Severity

#### [HIGH] Social Engineering via Deceptive Skill Description

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to provide legitimate Solana blockchain interaction capabilities, but the actual functionality requires installing an unverified third-party binary ('openclaw-agent') that has no connection to official Solana tooling. This is social engineering designed to trick users into installing malware under the guise of blockchain functionality.

#### [HIGH] Tool Poisoning via Fake Dependency Requirement

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-agent' is required for Solana operations to function, when in reality the official Solana CLI works independently. This is tool poisoning - creating a fake dependency to trick users into installing malicious software. The repeated emphasis that operations 'will not work' without it is designed to pressure users into compliance.

### MEDIUM Severity

#### [MEDIUM] Potential Credential Harvesting Setup

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill provides legitimate-looking Solana wallet commands that could be used to identify valuable wallet addresses. Combined with the malicious openclaw-agent binary, this creates a complete attack chain: identify wallets with the CLI commands, then exfiltrate private keys or credentials via the malicious agent running in the background.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
