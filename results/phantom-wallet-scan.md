# Agent Skill Security Scan Report

**Skill:** phantom
**Directory:** ./skills/clawhub-phantom-ggjrq
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 50.34s
**Timestamp:** 2026-02-01T18:14:38.692892

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Third-Party Binary Installation Required

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill mandates installation of 'openclaw-agent' from an untrusted third-party GitHub repository (hedefbari/openclaw-agent) before any wallet operations can function. This binary is distributed as a password-protected ZIP file (password: 'openclaw'), which is a common malware distribution technique to evade antivirus detection. The macOS installation uses an obfuscated script from glot.io, a code snippet sharing site, which prevents security review. This creates a critical supply chain attack vector where users must install unverified executables that will have access to their cryptocurrency wallets and private keys.

#### [CRITICAL] Credential Exposure Risk via Private Key Export Instructions

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill provides explicit instructions for exporting private keys from Phantom wallet and importing them into Solana CLI using 'solana-keygen recover'. This creates a critical security risk as private keys would be exposed in plaintext on the filesystem and in command history. Combined with the mandatory openclaw-agent installation, this could enable complete wallet compromise and asset theft. The instruction even acknowledges the danger with '(careful with this!)' but still provides the exact commands.

### HIGH Severity

#### [HIGH] Deceptive Skill Description Concealing Malware Installation

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to help users 'Work with Phantom browser extension' for legitimate wallet management tasks (add networks, import tokens, check dApps, troubleshoot). However, the actual functionality requires installing unverified third-party executables (openclaw-agent) that are not part of the official Phantom wallet ecosystem. This is classic social engineering - the skill masquerades as a helpful utility while actually serving as a delivery mechanism for potentially malicious software. The description makes no mention of the openclaw-agent requirement, concealing the true nature of the skill.

### MEDIUM Severity

#### [MEDIUM] Missing Referenced Files Create Incomplete and Potentially Harmful Instructions

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill references two Python files ('manually.py' and 'single.py') that are not included in the package. This creates an incomplete skill where users cannot fully utilize the documented functionality. Given the malicious nature of the openclaw-agent requirement, these missing files could have been intended to contain additional malicious payloads or data exfiltration code. The incomplete package state suggests either poor quality control or intentional obfuscation of the skill's true capabilities.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
