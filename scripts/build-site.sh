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
cp "$RESULTS_DIR"/*-scan.json "$SCANS_DIR/"

echo "Copied summary + $(ls "$SCANS_DIR"/*.json | wc -l | tr -d ' ') scan files to $DATA_DIR"
