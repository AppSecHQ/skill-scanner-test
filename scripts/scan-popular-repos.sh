#!/usr/bin/env bash
# Scan 10 popular GitHub skill repos identified from community research.
# Run from /workspace with API keys set.
set -euo pipefail

pip install -r scripts/requirements.txt --break-system-packages -q 2>/dev/null || true

python3 scripts/scan-skills.py \
  --repo-only \
  --repo trailofbits/skills \
  --repo kepano/obsidian-skills \
  --repo stripe/ai \
  --repo cloudflare/skills \
  --repo huggingface/skills \
  --repo SawyerHood/dev-browser \
  --repo lackeyjb/playwright-skill \
  --repo microsoft/agent-skills \
  --repo jthack/ffuf_claude_skill \
  --repo zxkane/aws-skills \
  --use-llm --enable-meta \
  -o results
