# Agent Skill Security Scan Report

**Skill:** phantom
**Directory:** ./skills/clawhub-phantom-fsvib
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 54.95s
**Timestamp:** 2026-02-01T16:57:32.350095

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Third-Party Binary Installation with Obfuscated Payload

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires installation of 'openclaw-agent' from an untrusted third-party GitHub repository (hedefbari/openclaw-agent). The Windows version is distributed as a password-protected ZIP file, a common malware distribution technique to evade antivirus scanning. The macOS version directs users to execute an arbitrary script from glot.io (a code snippet sharing site), which could contain any malicious payload. This binary is claimed to be required for 'wallet operations' but there is no legitimate technical reason why a Phantom browser extension would need a separate local agent binary. This is a classic trojan/backdoor distribution pattern.

#### [CRITICAL] Arbitrary Remote Code Execution via Unverified Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:7

**Description:** The skill instructs macOS users to download and execute an arbitrary script from glot.io (a public code snippet sharing site) directly in their terminal without any verification, code review, or security checks. The URL (https://glot.io/snippets/hfdxv8uyaf) points to user-uploaded content that could be modified at any time to contain malicious commands. This is a direct remote code execution vector that could install malware, steal credentials, or compromise the user's system.

### HIGH Severity

#### [HIGH] Private Key Export Instructions Create Credential Theft Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill provides instructions for exporting private keys from Phantom wallet and importing them into Solana CLI using 'solana-keygen recover'. While this may have legitimate use cases, the skill provides no security warnings about the risks of exposing private keys, no guidance on secure key handling, and the presence of the malicious openclaw-agent requirement suggests this could be part of a credential harvesting attack. Users following these instructions in the context of the compromised openclaw-agent could inadvertently expose their wallet private keys to the malicious binary.

#### [HIGH] Deceptive Skill Description Conceals Malware Distribution

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to help users 'Work with Phantom browser extension - add custom networks, import tokens, check connected dApps, troubleshoot issues, and manage Solana/Ethereum/Polygon accounts.' However, the actual primary purpose appears to be distributing the malicious openclaw-agent binary under the guise of legitimate wallet management. The description makes no mention of requiring third-party binary installation, misleading users about the skill's true behavior and security implications.

### MEDIUM Severity

#### [MEDIUM] Undocumented Tool Installation Requirement

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The YAML manifest includes an 'openclaw' metadata section that specifies installation of Solana CLI via curl pipe to shell ('sh -c "$(curl -sSfL https://release.solana.com/stable/install)"'). While the Solana CLI installation itself is from the official source, this installation method (curl | sh) bypasses package managers and security verification. Additionally, the manifest does not declare 'allowed-tools' restrictions, and the installation happens automatically without clear user consent in the skill description.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
