# Agent Skill Security Scan Report

**Skill:** paypal
**Directory:** /workspace/skills/clawhub-paypal
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 42.26s
**Timestamp:** 2026-02-06T06:13:18.444739

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Credential Exposure in Documentation

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill documentation instructs users to export PayPal API credentials (PAYPAL_CLIENT_ID and PAYPAL_SECRET) as environment variables. While this is a common pattern, the skill provides no implementation to securely handle these credentials. Without any script files to analyze, there's no way to verify secure credential handling, encryption, or proper API usage. The skill metadata indicates 'primaryEnv: PAYPAL_CLIENT_ID' suggesting credential dependency, but no code exists to validate secure usage.

### HIGH Severity

#### [HIGH] Missing Implementation - Tool Shadowing Risk

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill claims to provide PayPal payment integration with features like 'Send payments', 'Create invoices', 'Request money', 'Transaction history', and 'Refunds', but contains NO script files whatsoever. This creates a tool shadowing risk where the agent may attempt to fulfill these requests using other available tools (Bash, Python) in unsafe ways, potentially executing arbitrary commands to interact with PayPal APIs without proper validation, authentication, or security controls. The skill is essentially a hollow shell that could trick the agent into dangerous behavior.

#### [HIGH] Deceptive Skill Description - No Actual Implementation

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md:1

**Description:** The skill description claims 'PayPal payment integration. Send money, create invoices, and manage PayPal transactions.' but provides zero implementation. This is social engineering through deceptive metadata - users and agents are misled into believing this skill provides functional PayPal integration when it's actually an empty package. This could lead to failed transactions, security incidents if the agent improvises implementation, or user frustration.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
