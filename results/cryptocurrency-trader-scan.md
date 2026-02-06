# Agent Skill Security Scan Report

**Skill:** cryptocurrency-trader
**Directory:** /workspace/skills/clawhub-cryptocurrency-trader-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 68.00s
**Timestamp:** 2026-02-05T23:43:40.385751

## Summary

- **Total Findings:** 7
- **Critical:** 2
- **High:** 5
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Keys and Credential Exposure Risk

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/trading_agent.py

**Description:** The skill connects to cryptocurrency exchanges (Binance, Coinbase, Kraken) via ccxt library without any API key management or credential protection. While the current implementation uses public endpoints, the architecture is designed to support authenticated trading operations. The code lacks any credential validation, secure storage mechanisms, or warnings about API key exposure. Users may add API keys directly to the code, creating severe credential theft risks.

#### [CRITICAL] Unrestricted Network Access to External Cryptocurrency Exchanges

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/market/data_provider.py

**Description:** The skill makes unrestricted network calls to external cryptocurrency exchanges (binance.com, coinbase.com, kraken.com) without any user consent, rate limiting validation, or data exfiltration controls. The MarketDataProvider and MultiSourceDataAggregator components fetch real-time market data from multiple external sources. While ostensibly for market analysis, this architecture could be exploited to exfiltrate sensitive data (account balances, trading history, portfolio positions) to external servers.

### HIGH Severity

#### [HIGH] Infinite loop without clear exit condition

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** skill.py:181

**Description:** Pattern detected: while True:

#### [HIGH] Command Injection via Unvalidated Symbol Input

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** skill.py

**Description:** The skill accepts cryptocurrency trading pair symbols (e.g., 'BTC/USDT') as user input and passes them directly to exchange API calls and file operations without proper validation or sanitization. An attacker could inject malicious payloads via symbol parameters that could lead to command injection, path traversal, or code execution when symbols are used in file paths, logging, or system calls.

#### [HIGH] Unbounded Resource Consumption via Monte Carlo Simulations

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/advanced_analytics.py

**Description:** The skill performs Monte Carlo simulations with 10,000 iterations per analysis (advanced_analytics.py:45) without resource limits, timeouts, or user consent. Multiple concurrent analyses or market scans could trigger thousands of simulations simultaneously, causing CPU/memory exhaustion and denial of service. The MarketScanner can analyze 30+ symbols sequentially, each running 10,000 simulations.

#### [HIGH] Tool Restriction Violation - Undeclared Network and Python Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The SKILL.md manifest does not declare 'allowed-tools' but the skill extensively uses Python execution and network access (Bash for shell scripts, Python for exchange APIs). Per the agent skills specification, missing 'allowed-tools' is acceptable, but the skill's actual behavior (network calls, file I/O, subprocess execution) significantly exceeds what a user might expect from a 'trading analysis' tool. This represents tool capability deception.

#### [HIGH] Deceptive Skill Description - Production Trading vs Analysis Tool

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims 'production-grade AI trading agent for cryptocurrency markets' and 'designed for real-world trading application' but lacks critical production safeguards: no paper trading mode, no trade execution confirmation, no risk disclosure, no regulatory warnings, and no backtesting validation before live trading. The description misleads users into believing this is production-ready trading software when it's actually an experimental analysis tool.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
