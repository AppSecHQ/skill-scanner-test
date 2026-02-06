# Agent Skill Security Scan Report

**Skill:** excel
**Directory:** /workspace/skills/clawhub-excel-orp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 40.76s
**Timestamp:** 2026-02-06T00:59:04.592856

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Obfuscated Malicious Command Execution via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The macOS installation instructions contain a base64-encoded bash command that decodes to execute arbitrary code from an external server (http://91.92.242.30/q0c7ew2ro8l2cfqp). This is a classic malware delivery mechanism using obfuscation to hide malicious intent. The command downloads and executes unknown code without user visibility or consent.

#### [CRITICAL] Malicious External Code Execution from Untrusted Server

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:9

**Description:** The skill instructs users to execute code fetched from an external IP address (91.92.242.30) without any verification, signature checking, or transparency about what code will run. This is a direct data exfiltration and system compromise vector. The external server could deliver credential-stealing malware, backdoors, or ransomware.

### HIGH Severity

#### [HIGH] Social Engineering via Deceptive Skill Description

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate Excel manipulation tool but requires installation of 'openclaw-core' which is actually a malware delivery mechanism. The skill description makes no mention of the malicious installation requirements, deceiving users into thinking they're installing a safe productivity tool. The Windows download link uses password-protected archives (common malware evasion technique) and the macOS instructions use obfuscated commands.

#### [HIGH] Deceptive Installation Instructions with Malware Indicators

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The installation instructions exhibit multiple malware indicators: (1) Password-protected ZIP file ('openclaw') - common technique to evade antivirus scanning, (2) Download from GitHub releases without official repository verification, (3) Obfuscated base64 command for macOS, (4) Direct IP address instead of domain name, (5) Fake 'setup-service.com' domain in echo statement to appear legitimate while actual download is from IP address.

### MEDIUM Severity

#### [MEDIUM] Fake Dependency Requirement for Malware Installation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill claims to require 'openclaw-core' utility as a prerequisite, but this appears to be a fabricated dependency used as a social engineering vector to trick users into installing malware. There is no legitimate openclaw-core utility for Excel operations - Python libraries like openpyxl, pandas, or xlrd are the standard tools for Excel manipulation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
