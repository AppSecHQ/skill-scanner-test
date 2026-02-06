# Agent Skill Security Scan Report

**Skill:** foundry
**Directory:** /workspace/skills/clawhub-foundry
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 43.55s
**Timestamp:** 2026-02-06T01:32:07.077672

## Summary

- **Total Findings:** 6
- **Critical:** 2
- **High:** 3
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Arbitrary Code Execution via Self-Modification

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill explicitly enables self-modification capabilities through tools like 'foundry_add_tool' and 'foundry_add_hook' that can write new code into the agent's extension system. This allows the skill to inject arbitrary code that will be executed by the agent without user review or confirmation. The 'foundry_implement' tool performs end-to-end implementation including code execution.

#### [CRITICAL] Tool Poisoning via Extension Writing

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill can write new OpenClaw extensions and tools ('foundry_write_extension', 'foundry_add_tool') that will be loaded and executed by the agent system. This enables tool poisoning attacks where malicious tools can be injected into the agent's capability set, potentially replacing or shadowing legitimate tools.

### HIGH Severity

#### [HIGH] Unrestricted Network Access for Data Collection

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill enables fetching content from multiple external sources (docs.openclaw.ai, arXiv, GitHub) without restrictions. The 'foundry_research' and 'foundry_docs' tools can access arbitrary documentation URLs, and config enables arXiv and GitHub sources. This creates data exfiltration risks through unvalidated external content fetching.

#### [HIGH] Transitive Trust Abuse via External Documentation

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill automatically fetches and follows instructions from external sources (OpenClaw documentation, arXiv papers, GitHub repos) without validation. The 'autoLearn' feature set to true by default means the agent will automatically incorporate patterns from these external sources, creating indirect prompt injection risks.

#### [HIGH] Unbounded Autonomous Operation

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The 'foundry_implement' tool performs end-to-end implementation (research + write + deploy) without requiring user confirmation at each step. Combined with 'autoLearn: true', this creates unbounded autonomous behavior where the skill can continuously modify itself and the agent system without human oversight.

### MEDIUM Severity

#### [MEDIUM] Missing Dependency Provenance and Security

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill references multiple Python files (OpenClaw.py, arXiv.py, GitHub.py, etc.) that are not found in the package. The installation command 'openclaw plugins install @getfoundry/foundry-openclaw' downloads code from npm without version pinning or integrity verification. No license or provenance information is provided.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
