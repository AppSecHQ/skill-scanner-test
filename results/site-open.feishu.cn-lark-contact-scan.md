# Scan: lark-contact

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:12.552844+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | obfuscation | Hidden data file detected | .wellknown-origin.json |
| LOW | obfuscation | File extension does not match actual content type | SKILL.md |
| LOW | social_engineering | Skill description is too short | SKILL.md |
| INFO | policy_violation | Strict manifest load failed; inert fallback scan used | SKILL.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-contact-get-user.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-contact-search-bot.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-contact-search-user.md |
