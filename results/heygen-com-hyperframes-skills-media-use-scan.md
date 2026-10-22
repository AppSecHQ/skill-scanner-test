# Scan: media-use

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 116
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:35.418210+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | policy_violation | Moderate analyzability score |  |
| LOW | policy_violation | Skill package contains many files | . |
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/chime.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/chime.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/click-soft.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/click-soft.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/click.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/click.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/error.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/error.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/glitch-1.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/glitch-1.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/glitch-2.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/glitch-2.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/glitch-3.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/glitch-3.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/impact-bass-1.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/impact-bass-1.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/impact-bass-2.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/impact-bass-2.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/key-press.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/key-press.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/notification.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/notification.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/ping.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/ping.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/pop.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/pop.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/riser.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/riser.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/sparkle.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/sparkle.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/typing.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/typing.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/whoosh-cinematic.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/whoosh-cinematic.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/whoosh-short.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/whoosh-short.mp3 |
| MEDIUM | policy_violation | Unanalyzable binary file | audio/assets/sfx/whoosh.mp3 |
| INFO | policy_violation | Binary file detected in skill package | audio/assets/sfx/whoosh.mp3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/audio.test.mjs:4 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/audio.test.mjs:141 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/carve.mjs:27 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/carve.test.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/gemini-pipeline.test.mjs:6 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/gemini-pipeline.test.mjs:38 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/gemini-pipeline.test.mjs:60 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/gemini-pipeline.test.mjs:78 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/heygen-tts.test.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/heygen-tts.test.mjs:17 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/heygen-voice.test.mjs:35 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/audio-meta.test.mjs:14 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/audio-meta.test.mjs:110 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/bgm.mjs:14 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/bgm.mjs:35 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/bgm.mjs:45 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | audio/scripts/lib/bgm.mjs:232 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/gemini-auth.mjs:1 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/lib/gemini-auth.py:30 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/lib/gemini-auth.py:34 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/gemini-auth.test.mjs:1 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/gemini-auth.test.mjs:84 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | audio/scripts/lib/heygen.mjs:190 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/lib/heygen.test.mjs:222 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/python.mjs:18 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/python.mjs:26 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | audio/scripts/lib/sfx.test.mjs:142 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.cleanup.test.mjs:3 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:19 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:20 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:26 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:27 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:29 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.cleanup.test.mjs:37 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:44 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:85 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:88 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:90 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:93 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:104 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:107 |
| LOW | data_exfiltration | Node.js filesystem access candidate for sensitive-flow correlation | audio/scripts/lib/tts.cleanup.test.mjs:115 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.cleanup.test.mjs:129 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.mjs:17 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.mjs:33 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.mjs:111 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.mjs:116 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/lib/tts.mjs:223 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/wait-bgm.test.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | audio/scripts/wait-bgm.test.mjs:87 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/compatibility.test.mjs:4 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/dither.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/dither.test.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/dither.test.mjs:11 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/dither.test.mjs:12 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/dither.test.mjs:24 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/eval.mjs:18 |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/lib/npx-sync.mjs:20 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/lib/telemetry.mjs:13 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/lib/telemetry.mjs:163 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve-plugin.test.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve-plugin.test.mjs:24 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve-plugin.test.mjs:52 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve.mjs:16 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve.mjs:23 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/resolve.mjs:26 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcribe.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcribe.test.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcribe.test.mjs:91 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcript-cut.mjs:3 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcript-cut.test.mjs:2 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcript-cut.test.mjs:11 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcript-cut.test.mjs:12 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/transcript-cut.test.mjs:28 |
