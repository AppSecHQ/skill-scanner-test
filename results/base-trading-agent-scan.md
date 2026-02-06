# Agent Skill Security Scan Report

**Skill:** base-trading-agent
**Directory:** /workspace/skills/clawhub-base-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 42.67s
**Timestamp:** 2026-02-05T20:25:51.310274

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Payload Delivery via Obfuscated Base64 Command

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The macOS installation command contains a base64-encoded payload that decodes to a bash command fetching and executing arbitrary code from an external IP address (91.92.242.30). This is a classic malware delivery mechanism disguising a remote code execution attack as a legitimate setup step.

#### [CRITICAL] Suspicious Windows Executable with Password-Protected Archive

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs Windows users to download AuthTool.exe from an external GitHub repository, extract it with a hardcoded password (1234), and execute it. This is a common malware distribution pattern using password-protected archives to evade antivirus detection. The executable's purpose is not disclosed, and it's hosted on a suspicious repository (Aslaep123/clawd-authtool).

### HIGH Severity

#### [HIGH] Social Engineering via Deceptive Skill Description

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill masquerades as a legitimate DeFi trading agent for Base L2, using professional terminology and detailed feature descriptions to build false credibility. However, the actual functionality is malware delivery disguised as authentication/setup requirements. This is social engineering designed to trick users into executing malicious payloads.

#### [HIGH] Deceptive Critical Requirement Warnings

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses urgent warning boxes and 'CRITICAL REQUIREMENT' language to pressure users into executing malicious payloads without careful inspection. This psychological manipulation technique creates false urgency to bypass security skepticism.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
