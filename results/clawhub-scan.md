# Agent Skill Security Scan Report

**Skill:** clawhub
**Directory:** ./skills/clawhub-clawhub-rkvny
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 35.22s
**Timestamp:** 2026-02-01T19:27:12.104548

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Hardcoded Password

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs Windows users to download an executable (openclaw-agent.zip) from a third-party GitHub repository with a hardcoded password ('openclaw'). This is a classic malware distribution pattern: password-protected archives bypass antivirus scanning, and the executable has no provenance verification. The binary is presented as 'required' for all ClawHub operations, creating a dependency on untrusted code execution.

#### [CRITICAL] Remote Code Execution via Obfuscated Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:11

**Description:** The skill instructs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy an unknown script, and paste it directly into Terminal for execution. This is a textbook remote code execution attack vector. The script content is obfuscated (hosted externally), cannot be audited, and users are instructed to execute it blindly. The glot.io service is a code snippet sharing platform, not a trusted software distribution channel.

### HIGH Severity

#### [HIGH] Social Engineering via False Dependency Claims

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill repeatedly claims that 'openclaw-agent' is REQUIRED and that 'skill management operations will not work' without it. This creates artificial urgency and pressure to install the malicious binaries. The skill's actual functionality (clawhub CLI) is a legitimate npm package that does NOT require these external binaries. This is social engineering to trick users into compromising their systems.

#### [HIGH] Tool Poisoning via Malicious Dependency Injection

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill poisons the legitimate 'clawhub' npm package by injecting fake prerequisites (openclaw-agent binaries and scripts). The actual clawhub CLI tool is legitimate, but this skill wraps it with malicious installation instructions that compromise the user's system before the tool can be used. This is tool poisoning through dependency injection.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Description Concealing Malware Distribution

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims it helps 'search, install, update, and publish agent skills' but the actual content is primarily focused on tricking users into installing malware (openclaw-agent). The legitimate clawhub CLI functionality is buried beneath malicious installation instructions. This is deceptive content designed to appear helpful while delivering malware.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
