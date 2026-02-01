"""Tests for scripts/run_scans.py"""

import io
import json
import logging
import subprocess
import zipfile
from pathlib import Path
from unittest.mock import patch, MagicMock, ANY

import pytest
import requests

from run_scans import (
    sanitize_filename,
    parse_repo_arg,
    repo_to_dirname,
    find_skill_path,
    safe_extract,
    get_unique_repos,
    clone_repo,
    download_clawhub_skill,
    run_scan,
    scan_skills,
    scan_adhoc_repos,
)


class TestSanitizeFilename:
    def test_basic_name(self):
        assert sanitize_filename("my-skill") == "my-skill"

    def test_spaces_to_dashes(self):
        assert sanitize_filename("My Skill Name") == "my-skill-name"

    def test_special_characters_removed(self):
        assert sanitize_filename("My Skill (v2)") == "my-skill-v2"

    def test_multiple_dashes_collapsed(self):
        assert sanitize_filename("skill///with:::bad***chars") == "skill-with-bad-chars"

    def test_leading_trailing_stripped(self):
        assert sanitize_filename("  --spaces--  ") == "spaces"

    def test_empty_after_sanitize(self):
        result = sanitize_filename("***")
        assert result == ""

    def test_lowercase(self):
        assert sanitize_filename("MySkill") == "myskill"


class TestParseRepoArg:
    def test_owner_repo_format(self):
        assert parse_repo_arg("owner/repo") == "owner/repo"

    def test_full_https_url(self):
        assert parse_repo_arg("https://github.com/owner/repo") == "owner/repo"

    def test_https_with_git_suffix(self):
        assert parse_repo_arg("https://github.com/owner/repo.git") == "owner/repo"

    def test_github_com_without_protocol(self):
        assert parse_repo_arg("github.com/owner/repo") == "owner/repo"

    def test_whitespace_stripped(self):
        assert parse_repo_arg("  owner/repo  ") == "owner/repo"

    def test_invalid_format_raises(self):
        with pytest.raises(ValueError, match="Invalid repo format"):
            parse_repo_arg("just-a-name")

    def test_http_url_without_github(self):
        with pytest.raises(ValueError, match="Invalid repo format"):
            parse_repo_arg("https://gitlab.com/owner/repo")


class TestRepoToDirname:
    def test_basic(self):
        assert repo_to_dirname("owner/repo") == "owner-repo"

    def test_nested(self):
        assert repo_to_dirname("org/sub/repo") == "org-sub-repo"


class TestFindSkillPath:
    def test_skill_in_skills_subdir(self, tmp_path):
        skill_dir = tmp_path / "skills" / "my-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# Skill")
        result = find_skill_path(tmp_path, "my-skill")
        assert result == skill_dir

    def test_skill_at_repo_root(self, tmp_path):
        (tmp_path / "SKILL.md").write_text("# Skill")
        result = find_skill_path(tmp_path, "any-name")
        assert result == tmp_path

    def test_skill_not_found(self, tmp_path):
        result = find_skill_path(tmp_path, "nonexistent")
        assert result is None

    def test_normalized_prefix_removal(self, tmp_path):
        skill_dir = tmp_path / "skills" / "react-native"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# Skill")
        result = find_skill_path(tmp_path, "vercel-react-native")
        assert result == skill_dir


class TestSafeExtract:
    def test_safe_zip_extracts(self, tmp_path, make_zip):
        zf = make_zip({"hello.txt": "world", "sub/file.txt": "nested"})
        safe_extract(zf, tmp_path)
        assert (tmp_path / "hello.txt").read_text() == "world"
        assert (tmp_path / "sub" / "file.txt").read_text() == "nested"

    def test_path_traversal_blocked(self, tmp_path, make_zip):
        zf = make_zip({"../evil.txt": "malicious content"})

        with pytest.raises(ValueError, match="path traversal"):
            safe_extract(zf, tmp_path)

        assert not (tmp_path.parent / "evil.txt").exists()

    def test_deeply_nested_traversal_blocked(self, tmp_path, make_zip):
        zf = make_zip({"foo/../../evil.txt": "malicious"})

        with pytest.raises(ValueError, match="path traversal"):
            safe_extract(zf, tmp_path)


class TestGetUniqueRepos:
    def test_groups_by_repo(self, sample_skill_list):
        github_skills = [s for s in sample_skill_list if s.get("repo")]
        repos = get_unique_repos(github_skills)
        assert "owner/repo-a" in repos
        assert len(repos["owner/repo-a"]) == 2

    def test_empty_list(self):
        repos = get_unique_repos([])
        assert repos == {}


class TestCloneRepo:
    def test_skips_if_dest_exists(self, tmp_path):
        dest = tmp_path / "repo"
        dest.mkdir()
        with patch("run_scans.subprocess.run") as mock_run:
            result = clone_repo("owner/repo", dest)
        assert result is True
        mock_run.assert_not_called()

    @patch("run_scans.subprocess.run")
    def test_success(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0)
        dest = tmp_path / "repo"
        result = clone_repo("owner/repo", dest)
        assert result is True
        mock_run.assert_called_once()

    @patch("run_scans.subprocess.run")
    def test_failure(self, mock_run, tmp_path, caplog):
        mock_run.return_value = MagicMock(returncode=1, stderr="clone error")
        dest = tmp_path / "repo"
        with caplog.at_level(logging.ERROR):
            result = clone_repo("owner/repo", dest)
        assert result is False
        assert "Failed to clone" in caplog.text

    @patch("run_scans.subprocess.run")
    def test_timeout(self, mock_run, tmp_path, caplog):
        mock_run.side_effect = subprocess.TimeoutExpired(cmd="git", timeout=120)
        with caplog.at_level(logging.ERROR):
            result = clone_repo("owner/repo", tmp_path / "repo")
        assert result is False
        assert "timed out" in caplog.text

    @patch("run_scans.subprocess.run")
    def test_shallow_clone_uses_depth_flag(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0)
        clone_repo("owner/repo", tmp_path / "repo", shallow=True)
        cmd = mock_run.call_args[0][0]
        assert "--depth=1" in cmd

    @patch("run_scans.subprocess.run")
    def test_non_shallow_clone_no_depth_flag(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0)
        clone_repo("owner/repo", tmp_path / "repo", shallow=False)
        cmd = mock_run.call_args[0][0]
        assert "--depth=1" not in cmd


class TestDownloadClawhubSkill:
    def test_skips_if_dest_exists(self, tmp_path):
        dest = tmp_path / "skill"
        dest.mkdir()
        with patch("run_scans.get_session") as mock_get:
            result = download_clawhub_skill("my-slug", dest)
        assert result is True
        mock_get.assert_not_called()

    @patch("run_scans.get_session")
    def test_success(self, mock_get, tmp_path, make_zip):
        zip_bytes = make_zip({"SKILL.md": "# My Skill"}, as_bytes=True)
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.content = zip_bytes
        mock_session.get.return_value = mock_response
        mock_get.return_value = mock_session

        dest = tmp_path / "skill"
        result = download_clawhub_skill("my-slug", dest)
        assert result is True
        assert (dest / "SKILL.md").read_text() == "# My Skill"

    @patch("run_scans.get_session")
    def test_request_error(self, mock_get, tmp_path, caplog):
        mock_session = MagicMock()
        mock_session.get.side_effect = requests.RequestException("network error")
        mock_get.return_value = mock_session

        with caplog.at_level(logging.ERROR):
            result = download_clawhub_skill("my-slug", tmp_path / "skill")
        assert result is False
        assert "Failed to download" in caplog.text

    @patch("run_scans.get_session")
    def test_bad_zip(self, mock_get, tmp_path, caplog):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.content = b"not a zip file"
        mock_session.get.return_value = mock_response
        mock_get.return_value = mock_session

        with caplog.at_level(logging.ERROR):
            result = download_clawhub_skill("my-slug", tmp_path / "skill")
        assert result is False
        assert "Invalid ZIP" in caplog.text

    @patch("run_scans.get_session")
    def test_zip_slip_blocked(self, mock_get, tmp_path, make_zip, caplog):
        zip_bytes = make_zip({"../evil.txt": "malicious"}, as_bytes=True)
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.content = zip_bytes
        mock_session.get.return_value = mock_response
        mock_get.return_value = mock_session

        with caplog.at_level(logging.ERROR):
            result = download_clawhub_skill("my-slug", tmp_path / "skill")
        assert result is False
        assert "Unsafe ZIP" in caplog.text


class TestRunScan:
    @staticmethod
    def _mock_subprocess(json_output_path, scan_result):
        """Return a side_effect that writes JSON when the json format flag is present."""
        def side_effect(cmd, **kwargs):
            if "json" in cmd:
                json_output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(json_output_path, "w") as f:
                    json.dump(scan_result, f)
            return MagicMock(returncode=0)
        return side_effect

    @patch("run_scans.subprocess.run")
    def test_success(self, mock_run, tmp_path):
        skill_path = tmp_path / "skill"
        skill_path.mkdir()
        output_dir = tmp_path / "results"
        scan_data = {"skill_name": "test", "is_safe": True, "findings_count": 0}
        json_path = output_dir / "test-scan.json"

        mock_run.side_effect = self._mock_subprocess(json_path, scan_data)
        result = run_scan(skill_path, output_dir, "test")
        assert result == scan_data
        assert mock_run.call_count == 2  # JSON + Markdown

    @patch("run_scans.subprocess.run")
    def test_failure(self, mock_run, tmp_path, caplog):
        mock_run.return_value = MagicMock(returncode=1, stderr="scanner error")
        skill_path = tmp_path / "skill"
        skill_path.mkdir()
        with caplog.at_level(logging.ERROR):
            result = run_scan(skill_path, tmp_path / "results", "test")
        assert result is None
        assert "Scan failed" in caplog.text

    @patch("run_scans.subprocess.run")
    def test_timeout(self, mock_run, tmp_path, caplog):
        mock_run.side_effect = subprocess.TimeoutExpired(cmd="scan", timeout=300)
        skill_path = tmp_path / "skill"
        skill_path.mkdir()
        with caplog.at_level(logging.ERROR):
            result = run_scan(skill_path, tmp_path / "results", "test")
        assert result is None
        assert "timed out" in caplog.text


class TestScanSkills:
    @patch("run_scans.run_scan")
    @patch("run_scans.find_skill_path")
    @patch("run_scans.clone_repo")
    def test_github_skills(self, mock_clone, mock_find, mock_scan, tmp_path):
        mock_clone.return_value = True
        skill_path = tmp_path / "skill"
        mock_find.return_value = skill_path
        mock_scan.return_value = {"skill_name": "alpha", "is_safe": True, "findings_count": 0}

        skills = [{"rank": 1, "name": "alpha", "id": "alpha", "repo": "owner/repo", "source": "skills.sh"}]
        results = scan_skills(skills, tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["is_safe"] is True
        mock_clone.assert_called_once_with("owner/repo", tmp_path / "skills" / "owner-repo")
        mock_scan.assert_called_once_with(
            skill_path=skill_path,
            output_dir=tmp_path / "results",
            skill_name="alpha",
            scanner_path="skill-scanner",
            use_llm=False,
        )

    @patch("run_scans.run_scan")
    @patch("run_scans.download_clawhub_skill")
    def test_clawhub_skills(self, mock_download, mock_scan, tmp_path):
        mock_download.return_value = True
        mock_scan.return_value = {"skill_name": "gamma", "is_safe": True, "findings_count": 0}

        skill_dir = tmp_path / "skills" / "clawhub-gamma-slug"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# Skill")

        skills = [{"rank": 1, "name": "gamma", "id": "gamma-slug", "repo": None, "source": "clawhub"}]
        results = scan_skills(skills, tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        mock_download.assert_called_once_with("gamma-slug", skill_dir)
        mock_scan.assert_called_once()

    @patch("run_scans.run_scan")
    @patch("run_scans.find_skill_path")
    @patch("run_scans.clone_repo")
    def test_missing_skill_md(self, mock_clone, mock_find, mock_scan, tmp_path, caplog):
        mock_clone.return_value = True
        mock_find.return_value = None

        skills = [{"rank": 1, "name": "alpha", "id": "alpha", "repo": "owner/repo", "source": "skills.sh"}]
        with caplog.at_level(logging.WARNING):
            results = scan_skills(skills, tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["error"] == "SKILL.md not found"
        assert results[0]["is_safe"] is None
        mock_scan.assert_not_called()
        assert "SKILL.md not found" in caplog.text

    @patch("run_scans.run_scan")
    @patch("run_scans.clone_repo")
    def test_no_repo_specified(self, mock_clone, mock_scan, tmp_path, caplog):
        skills = [{"rank": 1, "name": "alpha", "id": "alpha", "repo": None, "source": "skills.sh"}]
        with caplog.at_level(logging.WARNING):
            results = scan_skills(skills, tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["error"] == "No repo specified"
        mock_scan.assert_not_called()
        assert "no repo" in caplog.text


class TestScanAdhocRepos:
    @patch("run_scans.run_scan")
    @patch("run_scans.clone_repo")
    def test_single_skill_in_repo(self, mock_clone, mock_scan, tmp_path):
        repo_dir = tmp_path / "skills" / "owner-repo"
        repo_dir.mkdir(parents=True)
        (repo_dir / "SKILL.md").write_text("# Skill")

        mock_clone.return_value = True
        mock_scan.return_value = {"skill_name": "owner-repo", "is_safe": True, "findings_count": 0}

        results = scan_adhoc_repos(["owner/repo"], tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["is_safe"] is True
        mock_clone.assert_called_once_with("owner/repo", repo_dir)

    @patch("run_scans.run_scan")
    @patch("run_scans.clone_repo")
    def test_multiple_skills_in_repo(self, mock_clone, mock_scan, tmp_path):
        repo_dir = tmp_path / "skills" / "owner-repo"
        for name in ["skill-a", "skill-b"]:
            skill_dir = repo_dir / name
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(f"# {name}")

        mock_clone.return_value = True
        mock_scan.return_value = {"skill_name": "test", "is_safe": True, "findings_count": 0}

        results = scan_adhoc_repos(["owner/repo"], tmp_path / "skills", tmp_path / "results")
        assert len(results) == 2
        assert mock_scan.call_count == 2

    @patch("run_scans.run_scan")
    @patch("run_scans.clone_repo")
    def test_clone_failure(self, mock_clone, mock_scan, tmp_path, caplog):
        mock_clone.return_value = False

        results = scan_adhoc_repos(["owner/repo"], tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["error"] == "Clone failed"
        mock_scan.assert_not_called()

    @patch("run_scans.run_scan")
    @patch("run_scans.clone_repo")
    def test_no_skill_md_found(self, mock_clone, mock_scan, tmp_path, caplog):
        repo_dir = tmp_path / "skills" / "owner-repo"
        repo_dir.mkdir(parents=True)
        mock_clone.return_value = True

        with caplog.at_level(logging.WARNING):
            results = scan_adhoc_repos(["owner/repo"], tmp_path / "skills", tmp_path / "results")
        assert len(results) == 1
        assert results[0]["error"] == "No SKILL.md found"
        mock_scan.assert_not_called()
        assert "No SKILL.md files found" in caplog.text

    def test_invalid_repo_arg(self, tmp_path, caplog):
        with caplog.at_level(logging.ERROR):
            results = scan_adhoc_repos(["not-a-repo"], tmp_path / "skills", tmp_path / "results")
        assert len(results) == 0
        assert "Invalid repo argument" in caplog.text
