"""Tests for scripts/generate_report.py"""

import json
from pathlib import Path

import pytest

from generate_report import _pct, aggregate_results, generate_markdown_report


class TestPct:
    def test_fifty_percent(self):
        assert _pct(5, 10) == "50%"

    def test_zero_of_nonzero(self):
        assert _pct(0, 10) == "0%"

    def test_division_by_zero(self):
        assert _pct(10, 0) == "0%"

    def test_hundred_percent(self):
        assert _pct(10, 10) == "100%"

    def test_rounding(self):
        assert _pct(1, 3) == "33%"


class TestAggregateResults:
    def test_empty_directory(self, tmp_results_dir):
        findings = aggregate_results(tmp_results_dir)
        assert findings["total_skills"] == 0
        assert findings["safe_skills"] == 0

    def test_with_scan_files(self, tmp_results_dir, sample_scan_result, safe_scan_result):
        with open(tmp_results_dir / "test-skill-scan.json", "w") as f:
            json.dump(sample_scan_result, f)
        with open(tmp_results_dir / "safe-skill-scan.json", "w") as f:
            json.dump(safe_scan_result, f)

        findings = aggregate_results(tmp_results_dir)

        assert findings["total_skills"] == 2
        assert findings["safe_skills"] == 1
        assert findings["unsafe_skills"] == 1
        assert findings["total_findings"] == 2
        assert findings["severity_counts"]["HIGH"] == 1
        assert findings["severity_counts"]["LOW"] == 1
        assert len(findings["top_risks"]) == 1

    def test_corrupted_json_counted_as_error(self, tmp_results_dir):
        (tmp_results_dir / "bad-scan.json").write_text("{invalid json")
        findings = aggregate_results(tmp_results_dir)
        assert findings["total_skills"] == 0
        assert findings["error_skills"] == 1

    def test_skills_sorted_by_findings_count(self, tmp_results_dir, sample_scan_result, safe_scan_result):
        with open(tmp_results_dir / "test-skill-scan.json", "w") as f:
            json.dump(sample_scan_result, f)
        with open(tmp_results_dir / "safe-skill-scan.json", "w") as f:
            json.dump(safe_scan_result, f)

        findings = aggregate_results(tmp_results_dir)
        # Skill with more findings should come first
        assert findings["skills"][0]["name"] == "test-skill"
        assert findings["skills"][1]["name"] == "safe-skill"


class TestGenerateMarkdownReport:
    def test_report_created(self, tmp_path, sample_scan_result, safe_scan_result):
        results_dir = tmp_path / "results"
        results_dir.mkdir()
        with open(results_dir / "test-skill-scan.json", "w") as f:
            json.dump(sample_scan_result, f)
        with open(results_dir / "safe-skill-scan.json", "w") as f:
            json.dump(safe_scan_result, f)

        findings = aggregate_results(results_dir)
        report_path = tmp_path / "report.md"
        generate_markdown_report(findings, report_path)

        assert report_path.exists()
        content = report_path.read_text()
        assert "Executive Summary" in content
        assert "test-skill" in content
        assert "safe-skill" in content

    def test_report_contains_top_risks(self, tmp_path, sample_scan_result):
        results_dir = tmp_path / "results"
        results_dir.mkdir()
        with open(results_dir / "test-skill-scan.json", "w") as f:
            json.dump(sample_scan_result, f)

        findings = aggregate_results(results_dir)
        report_path = tmp_path / "report.md"
        generate_markdown_report(findings, report_path)

        content = report_path.read_text()
        assert "Top Risks" in content
        assert "TEST_RULE_HIGH" in content
