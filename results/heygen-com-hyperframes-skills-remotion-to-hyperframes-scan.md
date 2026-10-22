# Scan: remotion-to-hyperframes

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 17
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:34.379268+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-1-title-card/remotion-src/package.json:9 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-1-title-card/remotion-src/package.json:10 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-1-title-card/remotion-src/package.json:11 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-1-title-card/remotion-src/package.json:12 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-2-multi-scene/remotion-src/package.json:9 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-2-multi-scene/remotion-src/package.json:10 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-2-multi-scene/remotion-src/package.json:11 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-2-multi-scene/remotion-src/package.json:12 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-3-data-driven/remotion-src/package.json:9 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-3-data-driven/remotion-src/package.json:10 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-3-data-driven/remotion-src/package.json:11 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-3-data-driven/remotion-src/package.json:12 |
| LOW | supply_chain_attack | Unpinned dependency | assets/test-corpus/tier-3-data-driven/remotion-src/package.json:13 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | assets/test-corpus/tier-4-escape-hatch/cases/03-async-metadata.tsx:31 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | assets/test-corpus/tier-4-escape-hatch/cases/08-mixed.tsx:25 |
| MEDIUM | obfuscation | File extension does not match actual content type | scripts/render_diff.sh |
