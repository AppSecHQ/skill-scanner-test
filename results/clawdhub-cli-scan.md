# Agent Skill Security Scan Report

**Skill:** clawdhub
**Directory:** /workspace/skills/clawhub-clawdhub-0mym4d53m7
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 34.68s
**Timestamp:** 2026-02-05T22:05:28.103553

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Obfuscated Remote Code Execution via Base64-Encoded Malicious Command

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The MacOS installation instructions contain a base64-encoded command that decodes to execute arbitrary code from a remote server (http://91.92.242.30/tjjve9itarrd3txw). This is a classic malware delivery mechanism using obfuscation to hide malicious intent. The command downloads and executes shell code from an untrusted external server without any verification or user visibility into what code is being run.

#### [CRITICAL] Social Engineering via Fake Dependency Requirement

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to require 'OpenClawProvider' as a dependency, presenting it as a legitimate prerequisite. However, the installation methods are highly suspicious (password-protected Windows archive, obfuscated MacOS command executing remote code). This appears to be social engineering to trick users into installing malware by disguising it as a required system component. The fake 'Setup-Wizard' URL and password-protected archive are classic malware distribution tactics.

### HIGH Severity

#### [HIGH] Suspicious External Server Communication

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The MacOS installation command contacts an IP address (91.92.242.30) rather than a legitimate domain name, which is a common indicator of malicious infrastructure. Legitimate software distributions use verified domains with HTTPS, not raw IP addresses with HTTP. The endpoint path (/tjjve9itarrd3txw) appears to be randomly generated, another indicator of malicious infrastructure designed to evade detection.

#### [HIGH] Deceptive Skill Description Masking Malware Delivery

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate CLI tool for managing agent skills from ClawdHub.com, but the actual content includes malware delivery mechanisms. The description focuses on benign functionality (search, install, update, publish skills) while hiding the malicious 'OpenClawProvider' installation instructions that deliver obfuscated remote code execution. This mismatch between stated purpose and actual behavior is a clear indicator of malicious intent.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
