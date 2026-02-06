# Agent Skill Security Scan Report

**Skill:** hyperliquid
**Directory:** /workspace/skills/clawhub-hyperliquid-cli
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 60.31s
**Timestamp:** 2026-02-06T03:17:48.193500

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Private Key Requirement with Direct Trading Access

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to provide their Hyperliquid private key (HYPERLIQUID_PRIVATE_KEY) which grants full control over trading accounts and funds. The private key is stored in plaintext in environment variables or local storage (~/.hyperliquid/accounts.db). This creates critical risks: (1) Private key exposure through environment variable leakage, (2) Unauthorized access to trading funds if the key is compromised, (3) No key rotation or revocation mechanism mentioned, (4) Direct financial loss potential through unauthorized trades. The skill executes real financial transactions with real money on a decentralized exchange using these credentials.

### HIGH Severity

#### [HIGH] Unbounded Autonomous Trading with Real Financial Risk

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill enables autonomous trading operations with real money on a decentralized exchange without explicit user confirmation requirements. The '--watch' mode provides real-time position monitoring, and the server mode enables sub-5ms latency trading, suggesting potential for high-frequency automated trading. There are no documented safeguards, transaction limits, or confirmation prompts before executing trades. An AI agent could potentially execute multiple trades rapidly, leading to significant financial losses through: (1) Unintended trade execution, (2) Market manipulation attempts, (3) Rapid position changes without oversight, (4) Leverage-induced liquidations (up to 50x leverage mentioned).

#### [HIGH] External Binary Dependency Without Verification

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires installation of an external npm package 'hyperliquid-cli' as a global binary ('hl') without any integrity verification, version pinning, or provenance checking. The installation command 'npm install -g hyperliquid-cli' pulls the latest version from npm without specifying a version hash or checksum. This creates supply chain risks: (1) Package could be compromised on npm registry, (2) Malicious updates could be automatically installed, (3) No verification of binary authenticity, (4) Global installation grants system-wide access, (5) The binary has direct access to private keys and can execute financial transactions.

### MEDIUM Severity

#### [MEDIUM] Misleading Scope - High-Frequency Trading Claims Without Safety Guardrails

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description prominently advertises 'sub-5ms low-latency high-frequency trading' and 'websocket client' capabilities, suggesting it's designed for automated high-frequency trading strategies. However, there are no documented safety mechanisms, risk management features, or trading limits appropriate for HFT scenarios. The description may mislead users into believing the skill is production-ready for automated trading when it lacks critical safeguards. High-frequency trading with real money requires sophisticated risk management, circuit breakers, and position limits that are not mentioned.

#### [MEDIUM] Persistent Server Mode with Unbounded Resource Consumption

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill includes a background server mode ('hl server start') that maintains persistent WebSocket connections and in-memory caching without documented resource limits, monitoring, or automatic shutdown mechanisms. The server runs indefinitely until manually stopped, potentially consuming system resources. There's no mention of: (1) Memory limits for caching, (2) Connection timeout policies, (3) Automatic restart on failure, (4) Resource monitoring or alerts, (5) Maximum cache size limits. A misbehaving server could exhaust system resources or maintain stale connections.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
