# Agent Skill Security Scan Report

**Skill:** api-gateway
**Directory:** /workspace/skills/clawhub-api-gateway
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 49.13s
**Timestamp:** 2026-02-05T19:57:14.146244

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Key Required in Authorization Header

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to provide a Maton API key in the Authorization header for all requests. While the skill instructs users to obtain their own API key from maton.ai/settings, this creates a critical security risk: users must expose their API keys to the agent, which could lead to credential theft if the agent's environment is compromised or if logs capture the Authorization headers. The API key provides access to third-party service connections (Slack, HubSpot, Salesforce, etc.), making it a high-value credential.

### HIGH Severity

#### [HIGH] Unrestricted Third-Party API Access via Passthrough Proxy

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill provides a passthrough proxy to numerous third-party APIs (Slack, HubSpot, Salesforce, Google Workspace, Stripe, QuickBooks, etc.) with no apparent restrictions on which endpoints can be called or what operations can be performed. The agent can make arbitrary API calls to any supported service using the user's authenticated connections. This creates tool exploitation risks: the agent could perform unauthorized operations like deleting data, modifying configurations, exfiltrating sensitive information, or making financial transactions without explicit user confirmation for each sensitive operation.

### MEDIUM Severity

#### [MEDIUM] Missing Security Warnings and Risk Disclosure

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description and documentation do not adequately warn users about the security implications of granting an AI agent broad access to third-party APIs. Users may not understand that they are giving the agent the ability to perform destructive operations, access sensitive data, or make financial transactions across multiple services. The skill presents itself as a convenient API gateway without highlighting the significant trust and security considerations involved.

#### [MEDIUM] SQL Injection Risk in QuickBooks Query Construction

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION

**Description:** The QuickBooks reference documentation shows SOQL query construction using URL parameters with user-provided search terms. If the agent constructs queries by directly concatenating user input into SOQL queries without proper sanitization, this could lead to SOQL injection attacks that could bypass access controls or extract unauthorized data.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
