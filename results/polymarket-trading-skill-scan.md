# Agent Skill Security Scan Report

**Skill:** polymarket
**Directory:** ./skills/clawhub-polymarket-qjypn
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.85s
**Timestamp:** 2026-02-01T19:09:44.571028

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
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

**Description:** The skill instructs users to download a binary executable (openclaw-agent.zip) from an untrusted GitHub repository with password-protected extraction (pass: 'openclaw'). This is a classic malware distribution pattern - password-protected archives bypass antivirus scanning, and the binary could contain arbitrary malicious code including keyloggers, credential stealers, or backdoors. The requirement to run this executable before any trading operations creates a dependency on untrusted code execution.

#### [CRITICAL] Malicious Script Execution via External URL

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:13

**Description:** The skill directs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf) and copy-paste a script directly into Terminal. This is an extremely dangerous pattern - the script content is not visible in the skill package, can be changed remotely at any time, and users are instructed to execute it with full shell privileges. This could install malware, steal credentials, exfiltrate data, or establish persistent backdoors.

### HIGH Severity

#### [HIGH] Deceptive Skill Purpose - Financial Fraud Risk

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to enable 'trading prediction markets on Polymarket' but requires installing untrusted third-party binaries ('openclaw-agent') that have no official relationship to Polymarket. The legitimate Polymarket platform does not require such tools. This appears to be a social engineering attack disguised as a trading utility, potentially designed to steal cryptocurrency wallet credentials, private keys, or trading account access.

#### [HIGH] Credential Harvesting via Environment Variable

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires the POLYMARKET_ADDRESS environment variable to be set, which likely contains wallet addresses or API credentials. Combined with the malicious binary requirement, this creates a complete attack chain: the untrusted executable could read this environment variable and exfiltrate wallet credentials or private keys to attacker-controlled servers.

### MEDIUM Severity

#### [MEDIUM] Shell Command Injection Risk in API Examples

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill provides bash examples using curl with variable substitution ($SLUG, $CONDITION_ID, $MARKET_ID) without any input validation or sanitization guidance. If users follow these examples with untrusted input, they could be vulnerable to command injection attacks where malicious input breaks out of the curl command and executes arbitrary shell commands.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
