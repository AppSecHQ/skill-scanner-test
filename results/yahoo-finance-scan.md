# Agent Skill Security Scan Report

**Skill:** yahoo-finance
**Directory:** ./skills/clawhub-yahoo-finance-bzrvt
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.39s
**Timestamp:** 2026-02-01T18:40:37.153958

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Obfuscated Payload

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version requires extracting with a password ('openclaw'), which is a common malware distribution technique to evade antivirus detection. The macOS version directs users to a third-party code execution site (glot.io) to run an installation script. This pattern is consistent with malware delivery - legitimate finance libraries do not require separate agent binaries. The yfinance Python library is legitimate and does not require any external agent to function.

#### [CRITICAL] Social Engineering via False Prerequisites

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive language claiming that 'Yahoo Finance operations require the openclaw-agent utility to function' and states 'Without openclaw-agent installed, stock data retrieval and financial operations will not work.' This is completely false - the yfinance Python library works independently without any external agent. This is a social engineering attack designed to trick users into installing malware by creating a false sense of necessity.

### HIGH Severity

#### [HIGH] Execution of Untrusted Remote Code via glot.io

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:8

**Description:** The macOS installation instructions direct users to visit glot.io (a code snippet sharing site), copy an unknown script, and paste it directly into Terminal for execution. This is a command injection vector where the attacker controls the script content at the remote URL. Users would be executing arbitrary code without any ability to verify its safety. The URL (https://glot.io/snippets/hfdxv8uyaf) could contain any malicious commands.

#### [HIGH] Password-Protected Archive for AV Evasion

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:7

**Description:** The Windows binary is distributed as a password-protected ZIP file (password: 'openclaw'). This is a well-known malware distribution technique used to evade antivirus scanning, as most AV engines cannot scan password-protected archives. Legitimate software is never distributed this way. This strongly indicates the payload is malicious and designed to bypass security controls.

### MEDIUM Severity

#### [MEDIUM] Tool Poisoning via Fake Dependency

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill's YAML metadata declares a dependency on 'openclaw-agent' in the openclaw.requires.bins field, falsely legitimizing the malicious binary as a required component. This poisons the skill's dependency chain by mixing a legitimate library (yfinance) with a fake malicious requirement. This could cause automated installation systems to attempt downloading the malware.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
