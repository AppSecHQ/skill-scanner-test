"""Tests for the community scan request handler."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from community_scan import (
    check_repo_size,
    format_results_comment,
    validate_repo,
    run_community_scan,
    MAX_COMMENT_LENGTH,
)


# --- validate_repo ---


class TestValidateRepo:
    """Tests for GitHub repo validation."""

    @patch("community_scan.requests.get")
    def test_valid_public_repo(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"private": False, "size": 1024}
        mock_get.return_value = mock_resp

        result = validate_repo("owner/repo")
        assert result["private"] is False
        mock_get.assert_called_once()

    @patch("community_scan.requests.get")
    def test_private_repo_exits(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"private": True, "size": 100}
        mock_get.return_value = mock_resp

        with pytest.raises(SystemExit):
            validate_repo("owner/private-repo")

    @patch("community_scan.requests.get")
    def test_not_found_exits(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 404
        mock_get.return_value = mock_resp

        with pytest.raises(SystemExit):
            validate_repo("owner/nonexistent")

    @patch("community_scan.requests.get")
    def test_api_error_exits(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_get.return_value = mock_resp

        with pytest.raises(SystemExit):
            validate_repo("owner/repo")

    @patch("community_scan.requests.get")
    def test_network_error_exits(self, mock_get):
        import requests
        mock_get.side_effect = requests.RequestException("connection failed")

        with pytest.raises(SystemExit):
            validate_repo("owner/repo")


# --- check_repo_size ---


class TestCheckRepoSize:
    """Tests for repository size validation."""

    def test_under_limit_passes(self):
        metadata = {"size": 100 * 1024}  # 100 MB in KB
        check_repo_size(metadata, 500, "owner/repo")  # Should not raise

    def test_over_limit_exits(self):
        metadata = {"size": 600 * 1024}  # 600 MB in KB
        with pytest.raises(SystemExit):
            check_repo_size(metadata, 500, "owner/repo")

    def test_exactly_at_limit_passes(self):
        metadata = {"size": 500 * 1024}  # 500 MB in KB
        check_repo_size(metadata, 500, "owner/repo")  # Should not raise

    def test_zero_size_passes(self):
        metadata = {"size": 0}
        check_repo_size(metadata, 500, "owner/repo")  # Should not raise


# --- format_results_comment ---


class TestFormatResultsComment:
    """Tests for result formatting."""

    def test_safe_skill_formatting(self, safe_scan_result):
        comment = format_results_comment("owner/repo", [safe_scan_result])
        assert "owner/repo" in comment
        assert "Safe | 1" in comment
        assert "Issues Found | 0" in comment

    def test_unsafe_skill_formatting(self, sample_scan_result):
        comment = format_results_comment("owner/repo", [sample_scan_result])
        assert "**No**" in comment
        assert "HIGH" in comment
        assert "Issues Found | 1" in comment

    def test_multiple_skills(self, safe_scan_result, sample_scan_result):
        comment = format_results_comment("owner/repo", [safe_scan_result, sample_scan_result])
        assert "Skills Found | 2" in comment
        assert "Safe | 1" in comment
        assert "Issues Found | 1" in comment

    def test_empty_results(self):
        comment = format_results_comment("owner/repo", [])
        assert "Skills Found | 0" in comment

    def test_error_result(self):
        error_result = {
            "skill_name": "broken",
            "is_safe": None,
            "error": "Scan failed",
            "findings_count": 0,
            "max_severity": "ERROR",
        }
        comment = format_results_comment("owner/repo", [error_result])
        assert "Errors | 1" in comment

    def test_truncation_on_long_output(self, sample_scan_result):
        # Create a result with many findings to exceed the limit
        big_result = dict(sample_scan_result)
        big_result["findings"] = sample_scan_result["findings"] * 500
        big_result["findings_count"] = len(big_result["findings"])

        comment = format_results_comment("owner/repo", [big_result])
        assert len(comment) <= MAX_COMMENT_LENGTH + 100  # Allow small margin

    def test_dashboard_link(self, safe_scan_result):
        comment = format_results_comment("owner/repo", [safe_scan_result])
        assert "skillscan.io" in comment

    def test_findings_detail_shown(self, sample_scan_result):
        comment = format_results_comment("owner/repo", [sample_scan_result])
        assert "command_injection" in comment
        assert "TEST_RULE_HIGH" in comment

    def test_findings_capped_at_20(self):
        finding = {
            "severity": "MEDIUM",
            "category": "test",
            "title": "Test finding",
            "description": "desc",
            "rule_id": "RULE",
        }
        result = {
            "skill_name": "big-skill",
            "is_safe": False,
            "max_severity": "MEDIUM",
            "findings_count": 30,
            "findings": [finding] * 30,
        }
        comment = format_results_comment("owner/repo", [result])
        assert "10 more findings" in comment


# --- run_community_scan ---


class TestRunCommunityScan:
    """Tests for the scan runner."""

    @patch("community_scan.run_scan")
    @patch("community_scan.clone_repo")
    def test_scan_with_skill_found(self, mock_clone, mock_scan, tmp_path):
        # Set up a fake repo with SKILL.md
        repo_dir = tmp_path / "skills" / "owner-repo"
        repo_dir.mkdir(parents=True)
        (repo_dir / "SKILL.md").write_text("# Test Skill")

        mock_clone.return_value = True
        mock_scan.return_value = {
            "skill_name": "owner-repo",
            "is_safe": True,
            "findings_count": 0,
            "findings": [],
            "max_severity": "SAFE",
        }

        results = run_community_scan(
            "owner/repo",
            skills_dir=tmp_path / "skills",
            output_dir=tmp_path / "results",
        )

        assert len(results) == 1
        assert results[0]["is_safe"] is True
        mock_clone.assert_called_once()
        mock_scan.assert_called_once()

    @patch("community_scan.clone_repo")
    def test_clone_failure_exits(self, mock_clone, tmp_path):
        mock_clone.return_value = False

        with pytest.raises(SystemExit):
            run_community_scan(
                "owner/repo",
                skills_dir=tmp_path / "skills",
                output_dir=tmp_path / "results",
            )

    @patch("community_scan.clone_repo")
    def test_no_skill_md_exits(self, mock_clone, tmp_path):
        # Clone succeeds but no SKILL.md
        repo_dir = tmp_path / "skills" / "owner-repo"
        repo_dir.mkdir(parents=True)
        (repo_dir / "README.md").write_text("# Not a skill")

        mock_clone.return_value = True

        with pytest.raises(SystemExit):
            run_community_scan(
                "owner/repo",
                skills_dir=tmp_path / "skills",
                output_dir=tmp_path / "results",
            )

    @patch("community_scan.run_scan")
    @patch("community_scan.clone_repo")
    def test_monorepo_multiple_skills(self, mock_clone, mock_scan, tmp_path):
        repo_dir = tmp_path / "skills" / "owner-repo"
        (repo_dir / "skills" / "alpha").mkdir(parents=True)
        (repo_dir / "skills" / "beta").mkdir(parents=True)
        (repo_dir / "skills" / "alpha" / "SKILL.md").write_text("# Alpha")
        (repo_dir / "skills" / "beta" / "SKILL.md").write_text("# Beta")

        mock_clone.return_value = True
        mock_scan.return_value = {
            "skill_name": "test",
            "is_safe": True,
            "findings_count": 0,
            "findings": [],
            "max_severity": "SAFE",
        }

        results = run_community_scan(
            "owner/repo",
            skills_dir=tmp_path / "skills",
            output_dir=tmp_path / "results",
        )

        assert len(results) == 2
        assert mock_scan.call_count == 2
