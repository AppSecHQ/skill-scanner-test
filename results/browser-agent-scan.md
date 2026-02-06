# Agent Skill Security Scan Report

**Skill:** browser-agent
**Directory:** /workspace/skills/clawhub-browser-agent-ed7
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.41s
**Timestamp:** 2026-02-05T20:52:54.557624

## Summary

- **Total Findings:** 6
- **Critical:** 3
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Injection via Base64-Encoded Remote Code Execution

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The macOS installation instructions contain a base64-encoded command that decodes to a bash command fetching and executing arbitrary code from a remote server (91.92.242.30). This is a classic remote code execution attack pattern where users are tricked into running malicious code under the guise of legitimate installation instructions. The command downloads and executes content from an untrusted external server without any verification.

#### [CRITICAL] Suspicious External Download from Untrusted Domain

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:13

**Description:** The Windows installation instructions direct users to download a password-protected archive from an untrusted GitHub repository (denboss99/openclaw-core). The use of password protection ('openclaw') is suspicious as legitimate open-source software does not typically require passwords for downloads. This pattern is commonly used to evade automated security scanning and deliver malware.

#### [CRITICAL] Social Engineering via Fake Dependency Requirement

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to require 'openclaw-core utility' which does not correspond to any legitimate browser automation tool. This is a social engineering tactic to trick users into installing malware by presenting it as a necessary dependency. Legitimate browser automation (Playwright, Puppeteer, Selenium) does not require such utilities and can be installed through standard package managers.

### HIGH Severity

#### [HIGH] Obfuscation via Base64 Encoding to Hide Malicious Intent

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:15

**Description:** The use of base64 encoding in the macOS installation command is a deliberate obfuscation technique to hide the malicious nature of the code from casual inspection. This prevents users from immediately recognizing that they are being instructed to download and execute arbitrary code from a remote server.

#### [HIGH] Deceptive Skill Description Masking Malware Delivery

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate browser automation tool with professional documentation and detailed API examples, but its true purpose is to deliver malware through fake installation instructions. The extensive documentation serves to build false credibility and distract from the malicious installation commands.

### MEDIUM Severity

#### [MEDIUM] Missing Script Implementation Creates Trust Void

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill references 'multiple.py' but provides no script files. This absence, combined with the malicious installation instructions, suggests the skill is incomplete or intentionally designed to rely on the malicious 'openclaw-core' binary for its actual functionality. Users cannot audit what the skill actually does.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
