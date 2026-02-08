#!/usr/bin/env bash
# Re-scan skills that failed due to credit exhaustion
# 163 skills need rescanning
#
# Features:
#   - Continues past individual failures
#   - Tracks progress for resumability
#   - Run again to resume from where it stopped
#   - Use --force to re-scan everything
set -uo pipefail

SCANNER="${SCANNER:-.venv/bin/skill-scanner}"
RESULTS_DIR="${RESULTS_DIR:-results}"
PROGRESS_FILE="${RESULTS_DIR}/.rescan-credit-progress"
FORCE="${1:-}"

# Counters
TOTAL=0
SKIPPED=0
SUCCESS=0
FAILED=0

# Load completed scans from progress file
declare -A COMPLETED
if [[ -f "$PROGRESS_FILE" && "$FORCE" != "--force" ]]; then
    while IFS= read -r stem; do
        COMPLETED["$stem"]=1
    done < "$PROGRESS_FILE"
    echo "Loaded ${#COMPLETED[@]} completed scans from progress file"
fi

echo "=== Credit Failure Rescan ==="
echo "Scanner: $SCANNER"
echo "Results: $RESULTS_DIR"
echo

scan_skill() {
    local path="$1"
    local stem="$2"
    local name="$3"

    TOTAL=$((TOTAL + 1))

    # Skip if already completed
    if [[ -n "${COMPLETED[$stem]:-}" ]]; then
        echo "[$TOTAL/163] SKIP: $name (already completed)"
        SKIPPED=$((SKIPPED + 1))
        return 0
    fi

    echo "[$TOTAL/163] Scanning: $name"

    local output_json="${RESULTS_DIR}/${stem}-scan.json"
    local output_log="${RESULTS_DIR}/${stem}-scan.log"

    if "$SCANNER" scan "$path" \
        --format json \
        --output "$output_json" \
        --use-llm \
        --enable-meta 2>&1 | tee "$output_log"; then
        echo "$stem" >> "$PROGRESS_FILE"
        SUCCESS=$((SUCCESS + 1))
        echo "[$TOTAL/163] SUCCESS: $name"
    else
        FAILED=$((FAILED + 1))
        echo "[$TOTAL/163] FAILED: $name"
    fi
    echo
}

# Skills list
scan_skill "/workspace/skills/antfu-skills/skills/vue" "vue" "vue"
scan_skill "/workspace/skills/anthropics-skills/skills/canvas-design" "skills-canvas-design" "skills-canvas-design"
scan_skill "/workspace/skills/anthropics-skills/skills/docx" "skills-docx" "skills-docx"
scan_skill "/workspace/skills/anthropics-skills/skills/frontend-design" "skills-frontend-design" "skills-frontend-design"
scan_skill "/workspace/skills/anthropics-skills/skills/internal-comms" "skills-internal-comms" "skills-internal-comms"
scan_skill "/workspace/skills/anthropics-skills/skills/slack-gif-creator" "skills-slack-gif-creator" "skills-slack-gif-creator"
scan_skill "/workspace/skills/anthropics-skills/skills/webapp-testing" "skills-webapp-testing" "skills-webapp-testing"
scan_skill "/workspace/skills/anthropics-skills/skills/web-artifacts-builder" "skills-web-artifacts-builder" "skills-web-artifacts-builder"
scan_skill "/workspace/skills/anthropics-skills/template" "template-skill" "template-skill"
scan_skill "/workspace/skills/clawhub-baidu-map-api" "调用百度地图api功能" "调用百度地图api功能"
scan_skill "/workspace/skills/clawhub-channel" "wechat-oa-channel" "wechat-oa-channel"
scan_skill "/workspace/skills/clawhub-context-manager" "smart-context-manager" "smart-context-manager"
scan_skill "/workspace/skills/clawhub-crypto-gold-monitor" "加密货币与贵金属监控" "加密货币与贵金属监控"
scan_skill "/workspace/skills/clawhub-kesslerio-stealth-browser" "stealth-browser" "stealth-browser"
scan_skill "/workspace/skills/clawhub-polymarket-4rrsh" "polymarket-better" "polymarket-better"
scan_skill "/workspace/skills/clawhub-polymarket-all-in-one" "polymarket-trading-skill" "polymarket-trading-skill"
scan_skill "/workspace/skills/clawhub-preview-markdown" "preview-markdown" "preview-markdown"
scan_skill "/workspace/skills/clawhub-primer-x402" "primer-x402" "primer-x402"
scan_skill "/workspace/skills/clawhub-qmd-external" "qmd-external-knowledge-base-search" "qmd-external-knowledge-base-search"
scan_skill "/workspace/skills/clawhub-querit-search" "querit-search" "querit-search"
scan_skill "/workspace/skills/clawhub-railway-skill" "railway" "railway"
scan_skill "/workspace/skills/clawhub-ralph-loop" "ralph-loop" "ralph-loop"
scan_skill "/workspace/skills/clawhub-react-email-skills" "react-email-skills" "react-email-skills"
scan_skill "/workspace/skills/clawhub-react-expert" "react-expert" "react-expert"
scan_skill "/workspace/skills/clawhub-readwise-mcp" "readwise" "readwise"
scan_skill "/workspace/skills/clawhub-reddit-scraper" "reddit-scraper" "reddit-scraper"
scan_skill "/workspace/skills/clawhub-redis" "redis" "redis"
scan_skill "/workspace/skills/clawhub-rei" "rei-clawd" "rei-clawd"
scan_skill "/workspace/skills/clawhub-remotion-video-toolkit" "remotion-video-toolkit" "remotion-video-toolkit"
scan_skill "/workspace/skills/clawhub-reposit" "reposit-collective-intelligence-for-ai-agents" "reposit-collective-intelligence-for-ai-agents"
scan_skill "/workspace/skills/clawhub-research-paper-writer" "research-paper-writer" "research-paper-writer"
scan_skill "/workspace/skills/clawhub-resume-builder" "resume-builder" "resume-builder"
scan_skill "/workspace/skills/clawhub-rssaurus" "rssaurus-agent-friendly-rss-feed-reader" "rssaurus-agent-friendly-rss-feed-reader"
scan_skill "/workspace/skills/clawhub-save-money" "save-money" "save-money"
scan_skill "/workspace/skills/clawhub-search-reddit" "search-reddit" "search-reddit"
scan_skill "/workspace/skills/clawhub-searxng" "searxng" "searxng"
scan_skill "/workspace/skills/clawhub-security-auditor" "security-auditor" "security-auditor"
scan_skill "/workspace/skills/clawhub-sendclaw" "sendclaw-email-without-human-permission" "sendclaw-email-without-human-permission"
scan_skill "/workspace/skills/clawhub-send-email" "send-email" "send-email"
scan_skill "/workspace/skills/clawhub-senior-architect" "senior-architect" "senior-architect"
scan_skill "/workspace/skills/clawhub-senior-devops" "senior-devops" "senior-devops"
scan_skill "/workspace/skills/clawhub-simmer" "simmer" "simmer"
scan_skill "/workspace/skills/clawhub-skill-creator-2" "skill-creator" "skill-creator"
scan_skill "/workspace/skills/clawhub-skill-scanner" "skillner" "skillner"
scan_skill "/workspace/skills/clawhub-slack-api" "slack" "slack"
scan_skill "/workspace/skills/clawhub-smtp-send" "smtp-send" "smtp-send"
scan_skill "/workspace/skills/clawhub-sora-2-nature-documentary" "sora-2-自然纪录片" "sora-2-自然纪录片"
scan_skill "/workspace/skills/clawhub-soulcraft" "soulcraft" "soulcraft"
scan_skill "/workspace/skills/clawhub-spring-boot-engineer" "spring-boot-engineer" "spring-boot-engineer"
scan_skill "/workspace/skills/clawhub-sql-assistant" "sql-assistant" "sql-assistant"
scan_skill "/workspace/skills/clawhub-sql-pro" "sql-pro" "sql-pro"
scan_skill "/workspace/skills/clawhub-ssh-essentials" "ssh-essentials" "ssh-essentials"
scan_skill "/workspace/skills/clawhub-startclaw-optimizer" "startclaw-optimizer" "startclaw-optimizer"
scan_skill "/workspace/skills/clawhub-stealthy-auto-browse" "stealthy-auto-browse" "stealthy-auto-browse"
scan_skill "/workspace/skills/clawhub-stock-evaluator" "stock-evaluator" "stock-evaluator"
scan_skill "/workspace/skills/clawhub-stock-market-pro" "stock-market-pro" "stock-market-pro"
scan_skill "/workspace/skills/clawhub-streme-launcher" "streme-token-launcher" "streme-token-launcher"
scan_skill "/workspace/skills/clawhub-supermemory" "supermemory" "supermemory"
scan_skill "/workspace/skills/clawhub-super-websearch-realtime" "realtime-web-search" "realtime-web-search"
scan_skill "/workspace/skills/clawhub-swarmmarket" "swarmmarket-skill,-make-money-with-your-agents" "swarmmarket-skill"
scan_skill "/workspace/skills/clawhub-swift-expert" "swift-expert" "swift-expert"
scan_skill "/workspace/skills/clawhub-system-monitor" "system-monitor" "system-monitor"
scan_skill "/workspace/skills/clawhub-taskmaster" "taskmaster-ai-cost-optimizer" "taskmaster-ai-cost-optimizer"
scan_skill "/workspace/skills/clawhub-taskr" "taskr-remote-task-tracking-for-ai-agents" "taskr-remote-task-tracking-for-ai-agents"
scan_skill "/workspace/skills/clawhub-technews" "techmeme-news" "techmeme-news"
scan_skill "/workspace/skills/clawhub-telegram-auto-topic" "telegram-auto-topic" "telegram-auto-topic"
scan_skill "/workspace/skills/clawhub-telegram-pairing-customization" "总是响应未配对用户的-start-消息-always-respond-to-start-messages-from-unpaired-users" "telegram-pairing"
scan_skill "/workspace/skills/clawhub-testing-sagb" "sagb" "sagb"
scan_skill "/workspace/skills/clawhub-test-skill-temp" "test-skill" "test-skill"
scan_skill "/workspace/skills/clawhub-test-specialist" "test-specialist" "test-specialist"
scan_skill "/workspace/skills/clawhub-tg" "telegram-cli" "telegram-cli"
scan_skill "/workspace/skills/clawhub-tinyfish-web-agent" "tinyfish-web-agent" "tinyfish-web-agent"
scan_skill "/workspace/skills/clawhub-tokenguard" "tokenguard" "tokenguard"
scan_skill "/workspace/skills/clawhub-trade-signal" "trade-singal" "trade-singal"
scan_skill "/workspace/skills/clawhub-trading-coach" "trading-coach" "trading-coach"
scan_skill "/workspace/skills/clawhub-transcribe" "transcribe" "transcribe"
scan_skill "/workspace/skills/clawhub-trmnl" "trmnl-display" "trmnl-display"
scan_skill "/workspace/skills/clawhub-twitter" "twitter" "twitter"
scan_skill "/workspace/skills/clawhub-ui-test" "ui-test" "ui-test"
scan_skill "/workspace/skills/clawhub-ui-ux-pro-max" "ui-ux-pro-max" "ui-ux-pro-max"
scan_skill "/workspace/skills/clawhub-undetectable-ai" "undetectable-ai" "undetectable-ai"
scan_skill "/workspace/skills/clawhub-update-plus" "update-plus" "update-plus"
scan_skill "/workspace/skills/clawhub-url-shortener" "url-shortener" "url-shortener"
scan_skill "/workspace/skills/clawhub-veo3-video-gen" "veo-3-video-gen-gemini-api" "veo-3-video-gen-gemini-api"
scan_skill "/workspace/skills/clawhub-vestaboard" "vestaboard" "vestaboard"
scan_skill "/workspace/skills/clawhub-video-agent" "video-agent" "video-agent"
scan_skill "/workspace/skills/clawhub-voice-agent" "voice-agent" "voice-agent"
scan_skill "/workspace/skills/clawhub-watch-my-money" "watch-my-money" "watch-my-money"
scan_skill "/workspace/skills/clawhub-webhook-gen" "webhook-generator" "webhook-generator"
scan_skill "/workspace/skills/clawhub-whisper" "whisper" "whisper"
scan_skill "/workspace/skills/clawhub-windows-control" "windows-control" "windows-control"
scan_skill "/workspace/skills/clawhub-wordpress-pro" "wordpress-pro" "wordpress-pro"
scan_skill "/workspace/skills/clawhub-x402" "x402" "x402"
scan_skill "/workspace/skills/clawhub-x-api" "x-api" "x-api"
scan_skill "/workspace/skills/clawhub-x-trends" "x-trends" "x-trends"
scan_skill "/workspace/skills/clawhub-x-trends-ngw4s" "x-twitter-trends" "x-twitter-trends"
scan_skill "/workspace/skills/clawhub-x-twitter" "x-twitter" "x-twitter"
scan_skill "/workspace/skills/clawhub-yahoo-finance-5tv" "yahoo-finance" "yahoo-finance"
scan_skill "/workspace/skills/clawhub-youtube-transcript" "youtube-transcript" "youtube-transcript"
scan_skill "/workspace/skills/clawhub-youtube-voice-summarizer-elevenlabs" "youtube-podcast-summarizer-via-elevenlabs" "youtube-podcast-summarizer"
scan_skill "/workspace/skills/clawhub-youtube-watchar" "youtube-watcher" "youtube-watcher"
scan_skill "/workspace/skills/clawhub-ytm-cast" "youtube-music-cast" "youtube-music-cast"
scan_skill "/workspace/skills/clawhub-yt-meta" "yt-meta-youtube-metadata-extractor" "yt-meta"
scan_skill "/workspace/skills/clawhub-yt-video-downloader" "youtube-video-downloader" "youtube-video-downloader"
scan_skill "/workspace/skills/clawhub-zoho-email-integration" "zoho-email-integration" "zoho-email-integration"
scan_skill "/workspace/skills/clawhub-zotero" "zotero" "zotero"
scan_skill "/workspace/skills/cloudflare-skills/skills/agents-sdk" "skills-agents-sdk" "skills-agents-sdk"
scan_skill "/workspace/skills/cloudflare-skills/skills/building-ai-agent-on-cloudflare" "skills-building-ai-agent-on-cloudflare" "skills-building-ai-agent-on-cloudflare"
scan_skill "/workspace/skills/cloudflare-skills/skills/building-mcp-server-on-cloudflare" "skills-building-mcp-server-on-cloudflare" "skills-building-mcp-server-on-cloudflare"
scan_skill "/workspace/skills/cloudflare-skills/skills/cloudflare" "skills-cloudflare" "skills-cloudflare"
scan_skill "/workspace/skills/cloudflare-skills/skills/durable-objects" "skills-durable-objects" "skills-durable-objects"
scan_skill "/workspace/skills/cloudflare-skills/skills/web-perf" "skills-web-perf" "skills-web-perf"
scan_skill "/workspace/skills/cloudflare-skills/skills/wrangler" "skills-wrangler" "skills-wrangler"
scan_skill "/workspace/skills/coreyhaines31-marketingskills/skills/popup-cro" "popup-cro" "popup-cro"
scan_skill "/workspace/skills/coreyhaines31-marketingskills/skills/referral-program" "referral-program" "referral-program"
scan_skill "/workspace/skills/coreyhaines31-marketingskills/skills/schema-markup" "schema-markup" "schema-markup"
scan_skill "/workspace/skills/coreyhaines31-marketingskills/skills/signup-flow-cro" "signup-flow-cro" "signup-flow-cro"
scan_skill "/workspace/skills/expo-skills/plugins/expo-app-design/skills/use-dom" "use-dom" "use-dom"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-cli" "skills-hugging-face-cli" "skills-hugging-face-cli"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-datasets" "skills-hugging-face-datasets" "skills-hugging-face-datasets"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-evaluation" "skills-hugging-face-evaluation" "skills-hugging-face-evaluation"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-jobs" "skills-hugging-face-jobs" "skills-hugging-face-jobs"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-model-trainer" "skills-hugging-face-model-trainer" "skills-hugging-face-model-trainer"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-paper-publisher" "skills-hugging-face-paper-publisher" "skills-hugging-face-paper-publisher"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-tool-builder" "skills-hugging-face-tool-builder" "skills-hugging-face-tool-builder"
scan_skill "/workspace/skills/huggingface-skills/skills/hugging-face-trackio" "skills-hugging-face-trackio" "skills-hugging-face-trackio"
scan_skill "/workspace/skills/kepano-obsidian-skills/skills/json-canvas" "skills-json-canvas" "skills-json-canvas"
scan_skill "/workspace/skills/kepano-obsidian-skills/skills/obsidian-bases" "skills-obsidian-bases" "skills-obsidian-bases"
scan_skill "/workspace/skills/kepano-obsidian-skills/skills/obsidian-markdown" "skills-obsidian-markdown" "skills-obsidian-markdown"
scan_skill "/workspace/skills/lackeyjb-playwright-skill/skills/playwright-skill" "skills-playwright-skill" "skills-playwright-skill"
scan_skill "/workspace/skills/obra-superpowers/skills/receiving-code-review" "receiving-code-review" "receiving-code-review"
scan_skill "/workspace/skills/obra-superpowers/skills/requesting-code-review" "requesting-code-review" "requesting-code-review"
scan_skill "/workspace/skills/obra-superpowers/skills/subagent-driven-development" "subagent-driven-development" "subagent-driven-development"
scan_skill "/workspace/skills/obra-superpowers/skills/using-git-worktrees" "using-git-worktrees" "using-git-worktrees"
scan_skill "/workspace/skills/obra-superpowers/skills/using-superpowers" "using-superpowers" "using-superpowers"
scan_skill "/workspace/skills/obra-superpowers/skills/verification-before-completion" "verification-before-completion" "verification-before-completion"
scan_skill "/workspace/skills/obra-superpowers/skills/writing-skills" "writing-skills" "writing-skills"
scan_skill "/workspace/skills/SawyerHood-dev-browser/skills/dev-browser" "skills-dev-browser" "skills-dev-browser"
scan_skill "/workspace/skills/softaworks-agent-toolkit/skills/qa-test-planner" "qa-test-planner" "qa-test-planner"
scan_skill "/workspace/skills/softaworks-agent-toolkit/skills/session-handoff" "session-handoff" "session-handoff"
scan_skill "/workspace/skills/softaworks-agent-toolkit/skills/ship-learn-next" "ship-learn-next" "ship-learn-next"
scan_skill "/workspace/skills/softaworks-agent-toolkit/skills/writing-clearly-and-concisely" "writing-clearly-and-concisely" "writing-clearly-and-concisely"
scan_skill "/workspace/skills/stripe-ai/skills/stripe-best-practices" "skills-stripe-best-practices" "skills-stripe-best-practices"
scan_skill "/workspace/skills/stripe-ai/skills/upgrade-stripe" "skills-upgrade-stripe" "skills-upgrade-stripe"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris" "plugins-testing-handbook-skills-skills-atheris" "atheris"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz" "plugins-testing-handbook-skills-skills-cargo-fuzz" "cargo-fuzz"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/codeql" "plugins-testing-handbook-skills-skills-codeql" "codeql"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing" "plugins-testing-handbook-skills-skills-constant-time-testing" "constant-time-testing"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis" "plugins-testing-handbook-skills-skills-coverage-analysis" "coverage-analysis"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary" "plugins-testing-handbook-skills-skills-fuzzing-dictionary" "fuzzing-dictionary"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles" "plugins-testing-handbook-skills-skills-fuzzing-obstacles" "fuzzing-obstacles"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing" "plugins-testing-handbook-skills-skills-harness-writing" "harness-writing"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl" "plugins-testing-handbook-skills-skills-libafl" "libafl"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/libfuzzer" "plugins-testing-handbook-skills-skills-libfuzzer" "libfuzzer"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz" "plugins-testing-handbook-skills-skills-ossfuzz" "ossfuzz"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy" "plugins-testing-handbook-skills-skills-ruzzy" "ruzzy"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/semgrep" "plugins-testing-handbook-skills-skills-semgrep" "semgrep"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator" "plugins-testing-handbook-skills-skills-testing-handbook-generator" "testing-handbook-generator"
scan_skill "/workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/wycheproof" "plugins-testing-handbook-skills-skills-wycheproof" "wycheproof"
scan_skill "/workspace/skills/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis" "plugins-variant-analysis-skills-variant-analysis" "variant-analysis"
scan_skill "/workspace/skills/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring" "plugins-yara-authoring-skills-yara-rule-authoring" "yara-rule-authoring"
scan_skill "/workspace/skills/vercel-turborepo/skills/turborepo" "turborepo" "turborepo"
scan_skill "/workspace/skills/wshobson-agents/plugins/frontend-mobile-development/skills/tailwind-design-system" "tailwind-design-system" "tailwind-design-system"

echo
echo "=== Complete ==="
echo "Total: $TOTAL | Skipped: $SKIPPED | Success: $SUCCESS | Failed: $FAILED"
echo
echo "Run: python3 scripts/generate_report.py -i $RESULTS_DIR"
