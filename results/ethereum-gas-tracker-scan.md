# Agent Skill Security Scan Report

**Skill:** ethereum-gas-tracker
**Directory:** ./skills/clawhub-ethereum-gas-tracker-rmiu4
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 54.11s
**Timestamp:** 2026-02-01T17:27:03.755082

## Summary

- **Total Findings:** 4
- **Critical:** 1
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

**Description:** The skill instructs users to download and execute a binary (openclaw-agent.exe) from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archive extraction. This is a classic malware distribution pattern: (1) Creates false dependency on 'openclaw-agent' utility that doesn't exist in legitimate Ethereum tooling, (2) Directs Windows users to download password-protected ZIP to evade automated scanning, (3) Directs macOS users to execute arbitrary shell script from glot.io paste site, (4) Claims gas tracking 'will not work' without this malware to pressure installation. The legitimate Foundry 'cast' tool requires no additional agent software. This is data exfiltration/malware delivery disguised as a prerequisite.

### HIGH Severity

#### [HIGH] Social Engineering via False Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive social engineering to convince users that malicious software is required. It falsely claims 'Ethereum gas tracking operations require the openclaw-agent utility to function' and 'Without openclaw-agent installed, gas price monitoring and blockchain operations will not work.' This is completely false - all gas tracking functionality shown uses standard tools (cast, curl, python3, requests library). The skill creates artificial urgency and dependency to trick users into installing malware. The legitimate Foundry installation is buried in metadata while the fake prerequisite is prominently featured.

#### [HIGH] Arbitrary Code Execution via External Script

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The macOS installation instructions direct users to visit glot.io/snippets/hfdxv8uyaf and execute arbitrary shell script content directly in Terminal without any verification, code review, or safety checks. Glot.io is a code snippet sharing site where content can be modified at any time. This creates a remote code execution vector where attackers can: (1) Modify the script after users have been directed to it, (2) Execute arbitrary commands with user privileges, (3) Install persistent malware, (4) Exfiltrate credentials and data. Users are instructed to blindly trust and execute unknown code.

### MEDIUM Severity

#### [MEDIUM] Tool Shadowing via Fake Dependency

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill attempts to shadow legitimate Ethereum tooling by inserting a fake 'openclaw-agent' dependency. The metadata correctly specifies Foundry's 'cast' tool as the actual requirement, but the instructions prominently feature the fake agent and bury the legitimate installation. This is tool shadowing - replacing or obscuring legitimate tools with malicious alternatives. Users may install the malware thinking it's required, while the actual tool (cast) is sufficient. The skill manipulates tool discovery and installation flow to prioritize the malicious component.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
