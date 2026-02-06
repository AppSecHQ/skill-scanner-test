# Agent Skill Security Scan Report

**Skill:** finance
**Directory:** /workspace/skills/clawhub-finance
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 36.98s
**Timestamp:** 2026-02-06T01:24:45.040901

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Network Data Transmission to External APIs

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/market_quote.py

**Description:** The skill makes network requests to external third-party APIs (ExchangeRate-API at open.er-api.com and Yahoo Finance via yfinance) to fetch financial data. While this is the intended functionality for a market tracking skill, it does transmit user queries (ticker symbols, currency pairs) to external services. The ExchangeRate-API endpoint is rate-limited and requires attribution per their terms of service, which is not mentioned in user-facing output.

### LOW Severity

#### [LOW] Potentially Misleading Real-Time Claims

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's description and instructions could mislead users about data freshness. While SKILL.md correctly warns 'Never claim real-time unless the provider is truly real-time' and notes 'FX updates daily', the skill name 'Market Tracker' and phrases like 'latest quotes' and 'what's the price now?' could create expectations of real-time data. Yahoo Finance via yfinance provides delayed quotes (typically 15-20 minutes), and FX data updates only once daily.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
