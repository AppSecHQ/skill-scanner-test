# Agent Skill Security Scan Report

**Skill:** Agent Browser
**Directory:** /workspace/skills/clawhub-agent-browser-fopzsipap75u
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 47.21s
**Timestamp:** 2026-02-05T20:58:18.590901

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Execution via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The MacOS installation instructions contain a base64-encoded command that decodes to a bash one-liner fetching and executing a script from an external IP address (91.92.242.30). This is a classic malware delivery pattern designed to execute arbitrary code from an attacker-controlled server. The obfuscation via base64 encoding is intended to hide the malicious payload from casual inspection.

#### [CRITICAL] Social Engineering via Fake Dependency Requirement

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'OpenClawProvider' is required to use agent-browser, directing users to download a password-protected archive from an unofficial GitHub repository (syazema/OpenClawProvider) or execute the malicious MacOS command. This is social engineering designed to trick users into installing malware by making it appear as a legitimate dependency. The legitimate agent-browser tool has no such requirement.

### HIGH Severity

#### [HIGH] Code Obfuscation to Conceal Malicious Intent

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:8

**Description:** The MacOS installation command uses base64 encoding to obfuscate a malicious payload. This obfuscation technique is specifically designed to bypass security reviews and hide the true nature of the command (remote code execution from an untrusted IP address). The use of obfuscation in installation instructions is a strong indicator of malicious intent.

#### [HIGH] Suspicious Password-Protected Archive from Unverified Source

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:5

**Description:** The Windows installation instructions direct users to download a password-protected ZIP file from an unofficial GitHub repository. Password-protected archives are commonly used by malware to evade antivirus scanning. The repository 'syazema/OpenClawProvider' is not associated with the legitimate vercel-labs/agent-browser project and the password ('openclaw') suggests this is a coordinated attack campaign.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Description Masking Malware Delivery

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description presents itself as legitimate documentation for the agent-browser tool, but the actual content is designed to deliver malware. This creates a false sense of legitimacy by mixing genuine agent-browser documentation with malicious installation instructions. Users may trust the skill because the bulk of the content appears legitimate.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
