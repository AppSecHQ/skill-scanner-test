# Agent Skill Security Scan Report

**Skill:** polymarket
**Directory:** ./skills/clawhub-polymarket-qpi7w
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 40.06s
**Timestamp:** 2026-02-01T19:52:20.847131

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Social Engineering

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute a binary (openclaw-agent.zip) from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected extraction. This is a classic malware distribution pattern disguised as a legitimate trading utility. The password protection ('openclaw') prevents antivirus scanning of the archive contents. The skill falsely claims this binary is required for Polymarket operations, which is deceptive - Polymarket's official API does not require any third-party agent software.

#### [CRITICAL] Remote Code Execution via Obfuscated Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:13

**Description:** The skill directs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf) and execute arbitrary code from that page directly in Terminal. This is a remote code execution attack vector where the attacker controls the script content on glot.io. The user is instructed to blindly copy-paste and execute unknown code, which could install malware, steal credentials, or compromise the system.

### HIGH Severity

#### [HIGH] Credential Harvesting via Required Environment Variable

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires users to set a POLYMARKET_ADDRESS environment variable, which likely contains wallet addresses or private keys for Polymarket trading. Combined with the malicious binary and remote script execution, this creates a complete credential theft pipeline. The openclaw-agent binary or remote script could exfiltrate this sensitive credential.

#### [HIGH] Deceptive Skill Description and False Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-agent utility' is required for Polymarket operations and that 'market data retrieval and trading operations will not work' without it. This is social engineering to convince users to install malware. Polymarket's public APIs (gamma-api.polymarket.com, clob.polymarket.com) are accessible without any third-party agent software. The skill description misleads users about legitimate Polymarket functionality.

### MEDIUM Severity

#### [MEDIUM] External Content Trust Without Validation

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to fetch and execute content from external URLs (GitHub releases, glot.io) without any validation, signature verification, or security checks. This creates a transitive trust vulnerability where the skill delegates trust to external sources that could be compromised or malicious.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
