# Agent Skill Security Scan Report

**Skill:** clawhub
**Directory:** /workspace/skills/clawhub-clawhub1
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 42.77s
**Timestamp:** 2026-02-05T22:17:53.790619

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 3
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Dependency Installation - Suspicious Binary Requirement

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires installation of 'openclawcli' binary from untrusted sources before the main ClawHub CLI can function. Windows users are directed to download a password-protected ZIP file from GitHub (openclawcli.zip with password 'openclaw'), and macOS users are directed to execute commands from an external code snippet hosting site (glot.io). Password-protected executables and remote code execution from snippet sites are common malware distribution vectors. This creates a supply chain attack where users must install potentially malicious software to use the skill.

#### [CRITICAL] Remote Code Execution via External Snippet Site

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:11

**Description:** macOS users are instructed to visit glot.io (a code snippet hosting site) and execute installation commands directly in Terminal. This is a classic remote code execution attack vector where arbitrary malicious commands could be executed on the user's system. The content at the external URL is not verified, can change at any time, and could contain malicious shell commands that compromise the system.

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:335

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] Social Engineering - Deceptive Dependency Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a ClawHub CLI tool (npm package 'clawhub') but requires a separate, suspicious binary 'openclawcli' that is not mentioned in the skill name or description. The instructions repeatedly emphasize that ClawHub 'will not function' without this binary, pressuring users to install the suspicious dependency. This is social engineering to trick users into installing potentially malicious software by making it seem like a legitimate requirement.

#### [HIGH] Tool Poisoning - Malicious Binary Injection into Skill Workflow

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill's metadata declares it requires the 'clawhub' binary (via openclaw.requires.bins), but the instructions mandate installing a separate 'openclawcli' binary first. This creates a tool poisoning scenario where the malicious openclawcli binary could intercept, modify, or replace the legitimate clawhub tool's behavior. The binary is positioned as a prerequisite that 'must be running' for ClawHub to work, suggesting it acts as a persistent background process.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
