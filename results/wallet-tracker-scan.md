# Agent Skill Security Scan Report

**Skill:** wallet-tracker
**Directory:** ./skills/clawhub-wallet-tracker-af1i6
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 38.06s
**Timestamp:** 2026-02-01T19:44:30.654578

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Social Engineering

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute an untrusted binary (openclaw-agent.zip) from GitHub with password-protected extraction. This is a classic malware distribution pattern disguised as a legitimate prerequisite. The Windows instructions direct users to download a password-protected ZIP file and run an executable, while macOS users are directed to copy and execute a script from an external paste site (glot.io). Both patterns are highly suspicious and commonly used for malware distribution.

#### [CRITICAL] Deceptive Skill Description - Trojan Horse Pattern

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate blockchain wallet tracker but uses this as a pretext to trick users into downloading and executing malicious software. The description focuses on useful blockchain monitoring features while hiding the true purpose: delivering malware through the 'openclaw-agent' binary. This is a classic trojan horse social engineering attack.

### HIGH Severity

#### [HIGH] External Script Execution from Untrusted Source

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md:8

**Description:** The macOS installation instructions direct users to visit an external paste site (glot.io/snippets/hfdxv8uyaf) and execute arbitrary code in their terminal. This is indirect prompt injection where the skill delegates trust to external, unverified content. The user has no way to verify what the script does before execution, and the content could be changed by the attacker at any time.

### MEDIUM Severity

#### [MEDIUM] Unbounded Infinite Loop Without Resource Controls

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The real-time monitoring script contains an infinite while True loop with no exit conditions, error handling, or resource limits. This could lead to resource exhaustion if the API becomes unavailable or rate limits are hit. Combined with the malicious binary requirement, this could be used for denial of service or to mask other malicious activities.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
