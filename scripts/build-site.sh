#!/usr/bin/env bash
# Copy scan result JSON into docs/data/ for the static site
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source and destination
RESULTS_DIR="${PROJECT_ROOT}/results"
DATA_DIR="${PROJECT_ROOT}/docs/data"
SCANS_DIR="${DATA_DIR}/scans"

# Create directories
mkdir -p "$SCANS_DIR"

# Copy summary
cp "$RESULTS_DIR/summary-report.json" "$DATA_DIR/summary.json"

# Copy individual scan files
cp "$RESULTS_DIR"/*-scan.json "$SCANS_DIR/" 2>/dev/null || true

# Copy dotfile scans with renamed filenames (GitHub Pages doesn't serve dotfiles)
for f in "$RESULTS_DIR"/.*-scan.json; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    # Remove leading dot
    newname="${base#.}"
    cp "$f" "$SCANS_DIR/$newname"
done

# Verify repo_url coverage (populated upstream by generate_report.py)
python3 -c "
import json
with open('${DATA_DIR}/summary.json') as f:
    summary = json.load(f)
total = len(summary.get('skills', []))
has_url = sum(1 for s in summary['skills'] if s.get('repo_url'))
print(f'repo_url coverage: {has_url}/{total} skills')
if has_url < total:
    missing = [s['name'] for s in summary['skills'] if not s.get('repo_url')]
    print(f'Missing: {missing}')
"

echo "Copied summary + $(ls "$SCANS_DIR"/*.json | wc -l | tr -d ' ') scan files to $DATA_DIR"
