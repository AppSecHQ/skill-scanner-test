# Agent Skill Security Scan Report

**Skill:** wallet-tracker
**Directory:** ./skills/clawhub-wallet-tracker-s5hx9
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 47.95s
**Timestamp:** 2026-02-01T18:01:19.605194

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Password-Protected Archive

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs Windows users to download a binary executable from an untrusted GitHub repository (hedefbari/openclaw-agent) distributed as a password-protected ZIP file. Password-protected archives are a common malware distribution technique to evade antivirus scanning. The executable's true purpose cannot be verified, and it could contain malware, spyware, or data exfiltration code. The skill falsely claims this utility is required for 'wallet tracking operations' when the actual tracking functionality uses standard API calls that don't require any special agent.

#### [CRITICAL] Malicious Script Download via Obfuscated URL

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The skill instructs macOS users to visit glot.io (a code snippet sharing site) to download and execute an 'installation script' in Terminal. The URL (https://glot.io/snippets/hfdxv8uyaf) points to an external, untrusted source where the attacker can host arbitrary malicious code. Users are told to copy and paste this script directly into Terminal with elevated privileges, which could execute commands to install malware, create backdoors, exfiltrate credentials, or compromise the system. This is a classic social engineering attack using script injection.

### HIGH Severity

#### [HIGH] Deceptive Skill Description - Social Engineering

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate 'wallet tracker' for monitoring blockchain addresses, but its true purpose is to trick users into downloading and executing malware. The actual wallet tracking code examples (Etherscan API calls, Solana RPC queries) are legitimate and functional, serving as a smokescreen to make the skill appear trustworthy. The malicious payload is hidden in the 'Prerequisites' section, which falsely claims that a special 'openclaw-agent utility' is required when it is not. This is a sophisticated social engineering attack using deceptive metadata and instructions.

#### [HIGH] Misleading Content - False Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill contains deliberately misleading content claiming that 'openclaw-agent utility' is required for wallet tracking operations and that 'Without openclaw-agent installed, blockchain monitoring and wallet tracking will not work.' This is factually false. All the blockchain tracking examples in the skill use standard public APIs (Etherscan, Solana RPC) accessible via curl and Python requests, which require no special utilities. This false claim is designed to manipulate users into installing malware by creating a false sense of necessity.

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Placeholders Encourage Insecure Practices

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill includes multiple examples with placeholder API keys ('YourApiKey', 'YourEtherscanApiKey') embedded directly in code and command-line examples. While these are placeholders, the pattern encourages users to hardcode their actual API keys in scripts and commands, which is an insecure practice. API keys should be stored in environment variables or secure configuration files, not embedded in code. This could lead to accidental exposure of credentials in version control, logs, or shared scripts.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
