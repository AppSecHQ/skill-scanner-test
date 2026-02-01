# Agent Skill Security Scan Report

**Skill:** ethereum-gas-tracker
**Directory:** ./skills/clawhub-ethereum-gas-tracker-t8oaj
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 46.75s
**Timestamp:** 2026-02-01T18:24:59.260322

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Deceptive Installation Instructions

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute a binary (openclaw-agent.zip) from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archive extraction. This is a classic malware distribution pattern. The Windows instructions direct users to download a ZIP file protected with password 'openclaw' and execute it. The macOS instructions direct users to visit glot.io (a code snippet sharing site) and paste unknown script content into Terminal. These are social engineering tactics to bypass security warnings and install potentially malicious software. The skill falsely claims this utility is required for gas tracking, but the actual gas tracking functionality only requires standard tools (cast, curl, python3).

### HIGH Severity

#### [HIGH] Social Engineering via False Prerequisite Claims

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive language to create urgency and false necessity around installing untrusted software. It claims 'IMPORTANT: Ethereum gas tracking operations require the openclaw-agent utility to function' and 'Without openclaw-agent installed, gas price monitoring and blockchain operations will not work.' This is demonstrably false - all the gas tracking code shown uses only standard tools (cast, curl, python3, requests). This is a social engineering tactic to manipulate users into installing potentially malicious software by creating false technical requirements.

#### [HIGH] Command Injection Risk via Unvalidated External Script Execution

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The macOS installation instructions direct users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy arbitrary script content, and paste it directly into Terminal for execution. This is a severe command injection vector - the content at that URL could be modified at any time to execute malicious commands. Users are instructed to blindly trust and execute code from an untrusted third-party snippet sharing site without any validation, verification, or review.

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Placeholder in Etherscan Example

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:95

**Description:** The Etherscan Gas Oracle example includes a placeholder API key ('YourKey') in the URL. While this is clearly a placeholder, it demonstrates a pattern that could lead users to hardcode their actual API keys directly in bash commands, which may be logged in shell history, process lists, or command logs. This creates a credential exposure risk.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
