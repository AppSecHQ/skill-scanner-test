# Agent Skill Security Scan Report

**Skill:** chromadb-memory
**Directory:** /workspace/skills/clawhub-chromadb-memory
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 40.61s
**Timestamp:** 2026-02-05T21:41:25.975589

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] ChromaDB Collection Poisoning Risk - No Integrity Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill trusts the ChromaDB collection contents without any integrity verification, provenance checking, or access controls. An attacker with access to the ChromaDB instance (localhost:8100) could poison the collection with malicious documents designed to manipulate agent behavior. The instructions explicitly state 'Use any ChromaDB-compatible indexer to populate your collection' without guidance on securing the collection or validating document sources. This creates a tool poisoning vector where the memory retrieval tool becomes a vehicle for injecting malicious content.

### LOW Severity

#### [LOW] Unencrypted Local Network Communication - Credential Exposure Risk

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill communicates with ChromaDB (localhost:8100) and Ollama (localhost:11434) over unencrypted HTTP. While these are localhost connections, this creates risks: 1) Credentials or sensitive data in ChromaDB could be exposed to local network sniffers. 2) No authentication is specified for ChromaDB access. 3) In containerized/VM environments, 'localhost' may traverse network boundaries. 4) The curl command in installation instructions uses HTTP without TLS verification.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
