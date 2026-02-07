#!/bin/bash
# Rescan skills that failed due to credit exhaustion
# 163 skills need rescanning

set -u

RESULTS_DIR="${1:-results}"
PROGRESS_FILE="$RESULTS_DIR/.rescan-credit-progress"

# Load completed scans
declare -A COMPLETED
if [ -f "$PROGRESS_FILE" ]; then
    while IFS= read -r line; do
        COMPLETED["$line"]=1
    done < "$PROGRESS_FILE"
fi

total=163
skipped=0
success=0
failed=0

scan_skill() {
    local skill_path="$1"
    local skill_name="$2"
    local output_file="$RESULTS_DIR/${skill_name}-scan.json"
    local log_file="$RESULTS_DIR/${skill_name}-scan.log"

    echo "Scanning: $skill_name"
    if python -m skill_scanner.cli scan "$skill_path" \
        --output-format json \
        --output "$output_file" \
        --llm \
        --meta 2>&1 | tee "$log_file"; then
        echo "$skill_name" >> "$PROGRESS_FILE"
        return 0
    else
        return 1
    fi
}

process_skill() {
    local skill_path="$1"
    local skill_name="$2"

    if [ "${COMPLETED[$skill_name]:-}" = "1" ]; then
        ((skipped++))
        return
    fi

    if scan_skill "$skill_path" "$skill_name"; then
        ((success++))
    else
        ((failed++))
    fi

    echo "Progress: $((skipped + success + failed))/$total"
}

echo "=== Credit Failure Rescan ==="
echo "Total: $total skills"
echo ""

# Skill list (skill_path skill_name pairs)
process_skill "/workspace/skills/antfu-skills/skills/vue" "vue"
process_skill "/workspace/skills/anthropics-skills/skills/canvas-design" "skills-canvas-design"
process_skill "/workspace/skills/anthropics-skills/skills/docx" "skills-docx"
process_skill "/workspace/skills/anthropics-skills/skills/frontend-design" "skills-frontend-design"
process_skill "/workspace/skills/anthropics-skills/skills/internal-comms" "skills-internal-comms"
process_skill "/workspace/skills/anthropics-skills/skills/slack-gif-creator" "skills-slack-gif-creator"
process_skill "/workspace/skills/anthropics-skills/skills/webapp-testing" "skills-webapp-testing"
process_skill "/workspace/skills/anthropics-skills/skills/web-artifacts-builder" "skills-web-artifacts-builder"
process_skill "/workspace/skills/anthropics-skills/template" "template-skill"
process_skill "/workspace/skills/clawhub-baidu-map-api" "调用百度地图api功能"
process_skill "/workspace/skills/clawhub-channel" "wechat-oa-channel"
process_skill "/workspace/skills/clawhub-context-manager" "smart-context-manager"
process_skill "/workspace/skills/clawhub-crypto-gold-monitor" "加密货币与贵金属监控"
process_skill "/workspace/skills/clawhub-kesslerio-stealth-browser" "stealth-browser"
process_skill "/workspace/skills/clawhub-polymarket-4rrsh" "polymarket-better"
process_skill "/workspace/skills/clawhub-polymarket-all-in-one" "polymarket-trading-skill"
process_skill "/workspace/skills/clawhub-preview-markdown" "preview-markdown"
process_skill "/workspace/skills/clawhub-primer-x402" "primer-x402"
process_skill "/workspace/skills/clawhub-qmd-external" "qmd-external-knowledge-base-search"
process_skill "/workspace/skills/clawhub-querit-search" "querit-search"
process_skill "/workspace/skills/clawhub-railway-skill" "railway"
process_skill "/workspace/skills/clawhub-ralph-loop" "ralph-loop"
process_skill "/workspace/skills/clawhub-react-email-skills" "react-email-skills"
process_skill "/workspace/skills/clawhub-react-expert" "react-expert"
process_skill "/workspace/skills/clawhub-readwise-mcp" "readwise"
process_skill "/workspace/skills/clawhub-reddit-scraper" "reddit-scraper"
process_skill "/workspace/skills/clawhub-redis" "redis"
process_skill "/workspace/skills/clawhub-rei" "rei-clawd"
process_skill "/workspace/skills/clawhub-remotion-video-toolkit" "remotion-video-toolkit"
process_skill "/workspace/skills/clawhub-reposit" "reposit-collective-intelligence-for-ai-agents"
process_skill "/workspace/skills/clawhub-research-paper-writer" "research-paper-writer"
process_skill "/workspace/skills/clawhub-resume-builder" "resume-builder"
process_skill "/workspace/skills/clawhub-rssaurus" "rssaurus-agent-friendly-rss-feed-reader"
process_skill "/workspace/skills/clawhub-save-money" "save-money"
process_skill "/workspace/skills/clawhub-search-reddit" "search-reddit"
process_skill "/workspace/skills/clawhub-searxng" "searxng"
process_skill "/workspace/skills/clawhub-security-auditor" "security-auditor"
process_skill "/workspace/skills/clawhub-sendclaw" "sendclaw-email-without-human-permission"
process_skill "/workspace/skills/clawhub-send-email" "send-email"
process_skill "/workspace/skills/clawhub-senior-architect" "senior-architect"
process_skill "/workspace/skills/clawhub-senior-devops" "senior-devops"
process_skill "/workspace/skills/clawhub-simmer" "simmer"
process_skill "/workspace/skills/clawhub-skill-creator-2" "skill-creator"
process_skill "/workspace/skills/clawhub-skill-scanner" "skillner"
process_skill "/workspace/skills/clawhub-slack-api" "slack"
process_skill "/workspace/skills/clawhub-smtp-send" "smtp-send"
process_skill "/workspace/skills/clawhub-sora-2-nature-documentary" "sora-2-自然纪录片"
process_skill "/workspace/skills/clawhub-soulcraft" "soulcraft"
process_skill "/workspace/skills/clawhub-spring-boot-engineer" "spring-boot-engineer"
process_skill "/workspace/skills/clawhub-sql-assistant" "sql-assistant"
process_skill "/workspace/skills/clawhub-sql-pro" "sql-pro"
process_skill "/workspace/skills/clawhub-ssh-essentials" "ssh-essentials"
process_skill "/workspace/skills/clawhub-startclaw-optimizer" "startclaw-optimizer"
process_skill "/workspace/skills/clawhub-stealthy-auto-browse" "stealthy-auto-browse"
process_skill "/workspace/skills/clawhub-stock-evaluator" "stock-evaluator"
process_skill "/workspace/skills/clawhub-stock-market-pro" "stock-market-pro"
process_skill "/workspace/skills/clawhub-streme-launcher" "streme-token-launcher"
process_skill "/workspace/skills/clawhub-supermemory" "supermemory"
process_skill "/workspace/skills/clawhub-super-websearch-realtime" "realtime-web-search"
process_skill "/workspace/skills/clawhub-swarmmarket" "swarmmarket-skill,-make-money-with-your-agents"
process_skill "/workspace/skills/clawhub-swift-expert" "swift-expert"
process_skill "/workspace/skills/clawhub-system-monitor" "system-monitor"
process_skill "/workspace/skills/clawhub-taskmaster" "taskmaster-ai-cost-optimizer"
process_skill "/workspace/skills/clawhub-taskr" "taskr-remote-task-tracking-for-ai-agents"
process_skill "/workspace/skills/clawhub-technews" "techmeme-news"
process_skill "/workspace/skills/clawhub-telegram-auto-topic" "telegram-auto-topic"
process_skill "/workspace/skills/clawhub-telegram-pairing-customization" "总是响应未配对用户的-start-消息-always-respond-to-start-messages-from-unpaired-users"
process_skill "/workspace/skills/clawhub-testing-sagb" "sagb"
process_skill "/workspace/skills/clawhub-test-skill-temp" "test-skill"
process_skill "/workspace/skills/clawhub-test-specialist" "test-specialist"
process_skill "/workspace/skills/clawhub-tg" "telegram-cli"
process_skill "/workspace/skills/clawhub-tinyfish-web-agent" "tinyfish-web-agent"
process_skill "/workspace/skills/clawhub-tokenguard" "tokenguard"
process_skill "/workspace/skills/clawhub-trade-signal" "trade-singal"
process_skill "/workspace/skills/clawhub-trading-coach" "trading-coach"
process_skill "/workspace/skills/clawhub-transcribe" "transcribe"
process_skill "/workspace/skills/clawhub-trmnl" "trmnl-display"
process_skill "/workspace/skills/clawhub-twitter" "twitter"
process_skill "/workspace/skills/clawhub-ui-test" "ui-test"
process_skill "/workspace/skills/clawhub-ui-ux-pro-max" "ui-ux-pro-max"
process_skill "/workspace/skills/clawhub-undetectable-ai" "undetectable-ai"
process_skill "/workspace/skills/clawhub-update-plus" "update-plus"
process_skill "/workspace/skills/clawhub-url-shortener" "url-shortener"
process_skill "/workspace/skills/clawhub-veo3-video-gen" "veo-3-video-gen-gemini-api"
process_skill "/workspace/skills/clawhub-vestaboard" "vestaboard"
process_skill "/workspace/skills/clawhub-video-agent" "video-agent"
process_skill "/workspace/skills/clawhub-voice-agent" "voice-agent"
process_skill "/workspace/skills/clawhub-watch-my-money" "watch-my-money"
process_skill "/workspace/skills/clawhub-webhook-gen" "webhook-generator"
process_skill "/workspace/skills/clawhub-whisper" "whisper"
process_skill "/workspace/skills/clawhub-windows-control" "windows-control"
process_skill "/workspace/skills/clawhub-wordpress-pro" "wordpress-pro"
process_skill "/workspace/skills/clawhub-x402" "x402"
process_skill "/workspace/skills/clawhub-x-api" "x-api"
process_skill "/workspace/skills/clawhub-x-trends" "x-trends"
process_skill "/workspace/skills/clawhub-x-trends-ngw4s" "x-twitter-trends"
process_skill "/workspace/skills/clawhub-x-twitter" "x-twitter"
process_skill "/workspace/skills/clawhub-yahoo-finance-5tv" "yahoo-finance"
process_skill "/workspace/skills/clawhub-youtube-transcript" "youtube-transcript"
process_skill "/workspace/skills/clawhub-youtube-voice-summarizer-elevenlabs" "youtube-podcast-summarizer-via-elevenlabs"
process_skill "/workspace/skills/clawhub-youtube-watchar" "youtube-watcher"
process_skill "/workspace/skills/clawhub-ytm-cast" "youtube-music-cast"
process_skill "/workspace/skills/clawhub-yt-meta" "yt-meta-youtube-metadata-extractor"
process_skill "/workspace/skills/clawhub-yt-video-downloader" "youtube-video-downloader"
process_skill "/workspace/skills/clawhub-zoho-email-integration" "zoho-email-integration"
process_skill "/workspace/skills/clawhub-zotero" "zotero"
process_skill "/workspace/skills/cloudflare-skills/skills/agents-sdk" "skills-agents-sdk"
process_skill "/workspace/skills/cloudflare-skills/skills/building-ai-agent-on-cloudflare" "skills-building-ai-agent-on-cloudflare"
process_skill "/workspace/skills/cloudflare-skills/skills/building-mcp-server-on-cloudflare" "skills-building-mcp-server-on-cloudflare"
process_skill "/workspace/skills/cloudflare-skills/skills/cloudflare" "skills-cloudflare"
process_skill "/workspace/skills/cloudflare-skills/skills/durable-objects" "skills-durable-objects"
process_skill "/workspace/skills/cloudflare-skills/skills/web-perf" "skills-web-perf"
process_skill "/workspace/skills/cloudflare-skills/skills/wrangler" "skills-wrangler"
process_skill "/workspace/skills/coreyhaines31-marketingskills/skills/popup-cro" "popup-cro"
process_skill "/workspace/skills/coreyhaines31-marketingskills/skills/referral-program" "referral-program"
process_skill "/workspace/skills/coreyhaines31-marketingskills/skills/schema-markup" "schema-markup"
process_skill "/workspace/skills/coreyhaines31-marketingskills/skills/signup-flow-cro" "signup-flow-cro"
process_skill "/workspace/skills/expo-skills/plugins/expo-app-design/skills/use-dom" "use-dom"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-cli" "skills-hugging-face-cli"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-datasets" "skills-hugging-face-datasets"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-evaluation" "skills-hugging-face-evaluation"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-jobs" "skills-hugging-face-jobs"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-model-trainer" "skills-hugging-face-model-trainer"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-paper-publisher" "skills-hugging-face-paper-publisher"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-tool-builder" "skills-hugging-face-tool-builder"
process_skill "/workspace/skills/huggingface-skills/skills/hugging-face-trackio" "skills-hugging-face-trackio"
process_skill "/workspace/skills/kepano-obsidian-skills/skills/json-canvas" "skills-json-canvas"
process_skill "/workspace/skills/kepano-obsidian-skills/skills/obsidian-bases" "skills-obsidian-bases"
process_skill "/workspace/skills/kepano-obsidian-skills/skills/obsidian-markdown" "skills-obsidian-markdown"
process_skill "/workspace/skills/lackeyjb-playwright-skill/skills/playwright-skill" "skills-playwright-skill"
process_skill "/workspace/skills/obra-superpowers/skills/receiving-code-review" "receiving-code-review"
process_skill "/workspace/skills/obra-superpowers/skills/requesting-code-review" "requesting-code-review"
process_skill "/workspace/skills/obra-superpowers/skills/subagent-driven-development" "subagent-driven-development"
process_skill "/workspace/skills/obra-superpowers/skills/using-git-worktrees" "using-git-worktrees"
process_skill "/workspace/skills/obra-superpowers/skills/using-superpowers" "using-superpowers"
process_skill "/workspace/skills/obra-superpowers/skills/verification-before-completion" "verification-before-completion"
process_skill "/workspace/skills/obra-superpowers/skills/writing-skills" "writing-skills"
process_skill "/workspace/skills/SawyerHood-dev-browser/skills/dev-browser" "skills-dev-browser"
process_skill "/workspace/skills/softaworks-agent-toolkit/skills/qa-test-planner" "qa-test-planner"
process_skill "/workspace/skills/softaworks-agent-toolkit/skills/session-handoff" "session-handoff"
process_skill "/workspace/skills/softaworks-agent-toolkit/skills/ship-learn-next" "ship-learn-next"
process_skill "/workspace/skills/softaworks-agent-toolkit/skills/writing-clearly-and-concisely" "writing-clearly-and-concisely"
process_skill "/workspace/skills/stripe-ai/skills/stripe-best-practices" "skills-stripe-best-practices"
process_skill "/workspace/skills/stripe-ai/skills/upgrade-stripe" "skills-upgrade-stripe"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris" "plugins-testing-handbook-skills-skills-atheris"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz" "plugins-testing-handbook-skills-skills-cargo-fuzz"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/codeql" "plugins-testing-handbook-skills-skills-codeql"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing" "plugins-testing-handbook-skills-skills-constant-time-testing"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis" "plugins-testing-handbook-skills-skills-coverage-analysis"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary" "plugins-testing-handbook-skills-skills-fuzzing-dictionary"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles" "plugins-testing-handbook-skills-skills-fuzzing-obstacles"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing" "plugins-testing-handbook-skills-skills-harness-writing"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl" "plugins-testing-handbook-skills-skills-libafl"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/libfuzzer" "plugins-testing-handbook-skills-skills-libfuzzer"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz" "plugins-testing-handbook-skills-skills-ossfuzz"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy" "plugins-testing-handbook-skills-skills-ruzzy"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/semgrep" "plugins-testing-handbook-skills-skills-semgrep"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator" "plugins-testing-handbook-skills-skills-testing-handbook-generator"
process_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/wycheproof" "plugins-testing-handbook-skills-skills-wycheproof"
process_skill "/workspace/skills/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis" "plugins-variant-analysis-skills-variant-analysis"
process_skill "/workspace/skills/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring" "plugins-yara-authoring-skills-yara-rule-authoring"
process_skill "/workspace/skills/vercel-turborepo/skills/turborepo" "turborepo"
process_skill "/workspace/skills/wshobson-agents/plugins/frontend-mobile-development/skills/tailwind-design-system" "tailwind-design-system"

echo ""
echo "=== Complete ==="
echo "Total: $total | Skipped: $skipped | Success: $success | Failed: $failed"
echo ""
echo "Run: python scripts/generate_report.py -i $RESULTS_DIR"
