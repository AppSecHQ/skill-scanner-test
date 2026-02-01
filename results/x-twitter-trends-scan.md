# Agent Skill Security Scan Report

**Skill:** x-trends
**Directory:** ./skills/clawhub-x-trends-rjmtk
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 42.91s
**Timestamp:** 2026-02-01T19:01:07.119802

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Obfuscated Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version is distributed as a password-protected ZIP file (password: 'openclaw'), a common malware distribution technique used to evade antivirus detection. The macOS version directs users to execute a script from glot.io (a code snippet sharing site), which is a classic social engineering attack vector. There is no legitimate reason for a Twitter trends skill to require a separate 'agent' binary - the official twurl CLI is sufficient for all Twitter API operations. This appears to be malware distribution disguised as a dependency.

#### [CRITICAL] Social Engineering Through Deceptive Dependency Claims

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill repeatedly claims that 'openclaw-agent must be running' for Twitter trends operations to work, which is completely false. The official Twitter API (accessed via twurl) does not require any third-party agent. This is a social engineering attack designed to trick users into installing malware by falsely claiming it's a required dependency. The skill uses authoritative language ('IMPORTANT', 'must be', 'will not work') to pressure users into compliance.

### HIGH Severity

#### [HIGH] Credential Theft Risk via Malicious Binary

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to authorize twurl with their Twitter API credentials (consumer key and secret) while also running the suspicious 'openclaw-agent' binary. A malicious agent running in the background could intercept these credentials during the authorization process, steal the OAuth tokens stored by twurl, or monitor API requests to exfiltrate user data and authentication tokens.

#### [HIGH] Remote Code Execution via Untrusted Script

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The macOS installation instructions direct users to visit glot.io (a code snippet sharing site) and execute an arbitrary script in their Terminal. This is a classic remote code execution attack vector. The script content is not shown in the skill documentation, users have no way to verify what code they're executing, and glot.io snippets can be modified by the attacker at any time. This allows arbitrary command execution with the user's privileges.

### MEDIUM Severity

#### [MEDIUM] Tool Poisoning Through Fake Dependency

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill poisons the legitimate Twitter trends workflow by injecting a fake dependency (openclaw-agent) into what should be a straightforward twurl-based operation. This is tool poisoning - corrupting a legitimate tool's usage pattern by adding malicious components. The skill's metadata even declares the fake dependency in the 'requires' field, lending false legitimacy to the malware.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
