# Agent Skill Security Scan Report

**Skill:** alby-bitcoin-payments-cli-skill
**Directory:** /workspace/skills/clawhub-alby-bitcoin-payments-cli-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 25.07s
**Timestamp:** 2026-02-05T19:00:21.464485

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Credential Storage Location Without Encryption

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store sensitive NWC connection secrets (nostr+walletconnect:// URLs) in plaintext files at predictable locations (~/.alby-cli/connection-secret.key). These connection secrets provide full access to bitcoin lightning wallets and can be used to send payments. Storing wallet credentials in plaintext files creates a significant data exposure risk if the user's system is compromised.

### MEDIUM Severity

#### [MEDIUM] External CLI Tool Execution Without Integrity Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill executes an external npm package (@getalby/cli) via npx without version pinning or integrity verification. The npx command downloads and executes code from npm registry at runtime. If the package is compromised, typosquatted, or maliciously updated, users could execute malicious code with access to their wallet credentials.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
