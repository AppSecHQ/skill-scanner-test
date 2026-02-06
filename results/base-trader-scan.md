# Agent Skill Security Scan Report

**Skill:** base-trader
**Directory:** /workspace/skills/clawhub-base-trader
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 50.30s
**Timestamp:** 2026-02-05T20:20:09.314741

## Summary

- **Total Findings:** 7
- **Critical:** 1
- **High:** 3
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Credential Path Exposure

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:13

**Description:** The skill hardcodes the path to Bankr API credentials at ~/.clawdbot/skills/bankr/config.json and references this configuration file multiple times. This creates a risk of credential exposure if the skill or logs are shared, and establishes a predictable target for credential theft.

### HIGH Severity

#### [HIGH] Unbounded Autonomous Trading Without Confirmation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill enables fully autonomous trading execution with real financial consequences without requiring explicit user confirmation for each trade. Instructions encourage automated strategies (DCA, limit orders, stop losses) that execute without user intervention, creating risk of unauthorized financial transactions.

#### [HIGH] No Rate Limiting or Resource Exhaustion Protection

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** references/automation-strategies.md

**Description:** The skill lacks any rate limiting, retry bounds, or protection against resource exhaustion. Automated trading strategies (DCA, TWAP, monitoring) could execute indefinitely without safeguards, potentially causing financial harm through excessive trading fees or unintended position accumulation.

#### [HIGH] Command Injection Risk in Trade Logging

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/log-trade.sh

**Description:** The log-trade.sh script uses unvalidated user input ($REASON parameter) directly in JSON construction and jq processing without proper sanitization. This could allow command injection if malicious content is passed as trade reasons.

### MEDIUM Severity

#### [MEDIUM] Deceptive Risk Framing and Gambling Encouragement

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** While the skill claims to prioritize 'capital preservation' and includes risk management guidelines, it actively encourages high-risk speculative trading ('launch sniping', leverage up to 50x, memecoin trading) with language that normalizes gambling behavior. The description uses trigger words like 'snipe', 'profit', 'PnL' to attract users to risky trading.

#### [MEDIUM] External Tool Dependency Without Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** scripts/check-portfolio.sh

**Description:** The skill depends entirely on an external Bankr tool located at ~/clawd/skills/bankr/scripts/bankr.sh but provides no verification of this tool's integrity, authenticity, or behavior. The skill blindly trusts and executes this external script with financial commands.

#### [MEDIUM] Sensitive Financial Data Logged Without Encryption

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/log-trade.sh

**Description:** The skill logs all trades including amounts, prices, and transaction hashes to an unencrypted JSON file (data/trades.json). This creates a persistent record of financial activity that could be exposed if the file system is compromised.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
