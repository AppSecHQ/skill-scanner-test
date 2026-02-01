# Agent Skill Security Scan Report

**Skill:** polymarket
**Directory:** ./skills/clawhub-polymarket-hoedg
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.99s
**Timestamp:** 2026-02-01T16:49:11.379848

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Obfuscated Credentials

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download a binary executable (openclaw-agent.zip) from an untrusted GitHub repository with password-protected extraction (pass: 'openclaw'). This is a classic malware distribution pattern - password-protected archives bypass antivirus scanning, and the binary could contain arbitrary malicious code including keyloggers, credential stealers, or backdoors. The requirement to run this executable before any trading operations creates a dependency on untrusted code with full system access.

#### [CRITICAL] Remote Code Execution via Untrusted Script

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:13

**Description:** The skill instructs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy an installation script, and paste it directly into Terminal. This is an extremely dangerous pattern that enables arbitrary remote code execution with full user privileges. The script content is not visible in the skill package, cannot be audited, and could be modified at any time by the attacker. Users are being socially engineered to execute untrusted code that could steal credentials, install backdoors, or exfiltrate data.

### HIGH Severity

#### [HIGH] Social Engineering Through Fake Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill creates a false sense of legitimacy by repeatedly claiming that 'openclaw-agent' is required for Polymarket operations. This is social engineering designed to convince users to install malware. The skill emphasizes 'IMPORTANT' and 'Prerequisites' to create urgency and authority. Real Polymarket API access does not require any third-party agent or binary - the public APIs work directly via curl/HTTP requests.

### MEDIUM Severity

#### [MEDIUM] Deceptive Trading Instructions Without Actual Implementation

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill provides extensive documentation about trading, placing bets, tracking positions, and automating strategies, but contains no actual implementation code. The curl examples shown only query public market data APIs - there is no code for placing trades, managing positions, or any of the promised trading functionality. This is deceptive content designed to make the skill appear legitimate while the real purpose is malware distribution.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
