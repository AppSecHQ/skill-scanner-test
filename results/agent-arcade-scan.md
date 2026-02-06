# Agent Skill Security Scan Report

**Skill:** agentarcade
**Directory:** /workspace/skills/clawhub-agent-arcade
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 42.26s
**Timestamp:** 2026-02-05T18:07:30.160004

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Credential Theft via Moltbook Credentials Access

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructions explicitly require reading Moltbook credentials from ~/.config/moltbook/credentials.json. This involves accessing potentially sensitive authentication tokens from the user's filesystem without clear justification for why the skill needs direct access to these credentials. The registration flow could be handled without requiring the agent to read stored credentials directly.

#### [HIGH] Hardcoded External API Integration with Credential Storage

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires storing AgentArcade API keys in ~/.config/agentarcade/credentials.json and making authenticated requests to agentarcade.gg. This creates a persistent credential store that could be accessed by other processes. The skill also requires posting verification messages to Moltbook, creating a chain of credential dependencies across multiple services.

### MEDIUM Severity

#### [MEDIUM] Social Engineering Game Mechanics Could Enable Prompt Injection Training

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's core purpose is teaching agents to 'trick' and 'socially engineer' other agents into saying target words. While framed as a game, this explicitly trains the agent in deceptive communication tactics and manipulation techniques that could be applied outside the game context. The description 'a game of social engineering and persuasion' normalizes manipulation behaviors.

#### [MEDIUM] Autonomous Gameplay via HEARTBEAT.md Integration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill includes a HEARTBEAT.md file designed for periodic autonomous execution without user interaction. This could cause the agent to automatically engage in matches, send messages, and make API calls in the background without explicit user approval for each action. The instruction 'Read skills/agentarcade/HEARTBEAT.md and follow it' delegates autonomous decision-making to an external file.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
