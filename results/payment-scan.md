# Agent Skill Security Scan Report

**Skill:** payment
**Directory:** /workspace/skills/clawhub-payment
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 41.84s
**Timestamp:** 2026-02-06T06:10:15.966899

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Deceptive Skill Description - No Implementation Provided

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING

**Description:** The skill claims to provide 'Payment processing and management' with features like 'Create and send invoices', 'Process payments', 'Track payment status', and 'Refund management' across multiple payment gateways (Stripe, PayPal, Square, Crypto). However, NO implementation files (Python/Bash scripts) are included in the package. This is a form of social engineering where the skill misleads users about its actual capabilities. Users may believe they have a functional payment processing tool when they have none, potentially leading to failed transactions, business disruptions, or reliance on non-existent functionality.

### MEDIUM Severity

#### [MEDIUM] Missing Implementation Creates Security Risk for Sensitive Operations

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill declares it handles highly sensitive financial operations (payment processing, invoices, transactions, refunds) but provides no code implementation. This creates a security risk because: 1) Users may attempt to use the skill for real financial transactions, expecting secure handling that doesn't exist, 2) The absence of implementation means no security controls, validation, or encryption are in place for payment data, 3) The skill's metadata indicates it 'requires' curl and jq (external binaries), suggesting network operations were intended but not implemented, potentially leaving users vulnerable if they manually implement based on incomplete guidance.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
