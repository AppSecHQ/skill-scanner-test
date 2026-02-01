# Agent Skill Security Scan Report

**Skill:** yahoo-finance
**Directory:** ./skills/clawhub-yahoo-finance-jzgua
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 33.60s
**Timestamp:** 2026-02-01T19:35:45.614143

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Social Engineering

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute an untrusted binary (openclaw-agent.zip) from GitHub with password-protected extraction. This is a classic malware distribution pattern disguised as a legitimate prerequisite. The binary's purpose is unclear and unrelated to Yahoo Finance functionality, which only requires the yfinance Python package.

#### [CRITICAL] Remote Code Execution via External Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:7

**Description:** The skill instructs macOS users to visit an external URL (glot.io) and execute an arbitrary script in their terminal. This is a direct remote code execution vector where users blindly execute untrusted code from an external source. The script content is not disclosed, auditable, or version-controlled.

### HIGH Severity

#### [HIGH] Deceptive Prerequisites - Fake Dependency

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-agent utility' is required for Yahoo Finance operations to function. This is completely false - the yfinance Python library works independently without any additional agent or binary. This deception is used to trick users into installing malware.

#### [HIGH] Misleading Installation Instructions

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents malicious binary installation as a legitimate prerequisite, using authoritative language ('IMPORTANT', 'will not work') to pressure users into compliance. This is deceptive content designed to manipulate user behavior and bypass security skepticism.

### MEDIUM Severity

#### [MEDIUM] Password-Protected Archive - Obfuscation Technique

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:5

**Description:** The malicious binary is distributed as a password-protected ZIP file (password: 'openclaw'). This is a common malware distribution technique to evade automated security scanning, antivirus detection, and email filters. Legitimate software does not require password-protected archives.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
