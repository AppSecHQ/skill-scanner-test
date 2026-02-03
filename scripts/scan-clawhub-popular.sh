#!/usr/bin/env bash
# Scan popular clawhub.ai skills not yet in our results.
# Downloads each via the clawhub API and scans with full pipeline.
# Run from /workspace with API keys set.
set -euo pipefail

pip install -r scripts/requirements.txt --break-system-packages -q 2>/dev/null || true

# Fetch top 300 from clawhub (no offset — re-fetches full list to catch
# any popular skills that were added since our earlier runs).
# Already-cloned skills are skipped automatically; only new ones download.
python3 scripts/scan-skills.py \
  --source clawhub \
  -n 300 \
  --use-llm --enable-meta \
  -o results
