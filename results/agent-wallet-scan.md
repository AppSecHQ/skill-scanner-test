# Agent Skill Security Scan Report

**Skill:** Agent Wallet
**Directory:** ./skills/clawhub-agent-wallet
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 41.98s
**Timestamp:** 2026-02-01T09:00:59.625821

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Key Storage and Transmission Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store API keys that control blockchain wallet operations with real financial value. The API key provides full access to execute transactions within policy limits. The instructions tell users to 'store this securely' but provide no guidance on secure storage mechanisms, and the key is transmitted as a Bearer token in plain HTTP headers. If the API key is compromised, an attacker could drain funds within the configured policy limits.

### MEDIUM Severity

#### [MEDIUM] External API Dependency Without Provenance Verification

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill relies entirely on external API endpoints (safeskill-production.up.railway.app) for all wallet operations including transaction signing and execution. There is no verification of API endpoint authenticity, no certificate pinning, and no integrity checks. The API URL can be overridden via environment variables (SAFESKILLS_API_URL), which could enable man-in-the-middle attacks or redirection to malicious endpoints that could steal funds or API keys.

#### [MEDIUM] No Rate Limiting or Resource Constraints Documented

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill provides API endpoints for financial transactions but includes no documentation of rate limiting, transaction throttling, or resource constraints. An agent could potentially execute unlimited API calls, leading to resource exhaustion, unexpected costs, or denial of service. The transfer endpoint could be called repeatedly without documented safeguards, potentially draining wallet funds faster than intended even within policy limits.

### LOW Severity

#### [LOW] Incomplete Documentation of Security Model

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** While the skill claims 'The agent never sees the private key' and mentions 'spending policies', the actual security model, policy enforcement mechanisms, and trust boundaries are not fully documented. Users cannot verify how policies are enforced, what happens if policies are violated, or what protections exist against policy bypass. This lack of transparency makes it difficult for users to assess the actual security guarantees.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
