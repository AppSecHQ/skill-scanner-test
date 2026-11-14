"""Tests for the community scan request handler."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from community_scan import (
    dedupe_identical_skill_dirs,
    run_second_scanner,
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

    @patch("community_scan.run_batch_scan", return_value=None)  # force per-skill fallback path
    @patch("community_scan.run_scan")
    @patch("community_scan.clone_repo")
    def test_scan_with_skill_found(self, mock_clone, mock_scan, mock_batch, tmp_path):
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

    @patch("community_scan.run_batch_scan", return_value=None)  # force per-skill fallback path
    @patch("community_scan.run_scan")
    @patch("community_scan.clone_repo")
    def test_monorepo_multiple_skills(self, mock_clone, mock_scan, mock_batch, tmp_path):
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


# --- byte-identical copies within one repo ---


class TestDedupeIdenticalSkillDirs:
    def _skill(self, d, body="# x", extra=None):
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(body)
        if extra:
            (d / "references").mkdir()
            (d / "references" / "contract.json").write_text(extra)
        return d

    def test_shallowest_identical_dir_wins(self, tmp_path):
        repo = tmp_path / "repo"
        canon = self._skill(repo / "skills" / "a", extra="{}")
        copy1 = self._skill(repo / "plugins" / "p1" / "skills" / "a", extra="{}")
        copy2 = self._skill(repo / "plugins" / "p2" / "skills" / "a", extra="{}")
        other = self._skill(repo / "skills" / "b", body="# different")
        kept, copies = dedupe_identical_skill_dirs([copy1, canon, copy2, other], repo)
        assert kept == [canon, other]  # original order, copies dropped
        assert copies == {copy1: canon, copy2: canon}

    def test_same_files_under_different_names_are_distinct_skills(self, tmp_path):
        repo = tmp_path / "repo"
        a = self._skill(repo / "skills" / "a")
        b = self._skill(repo / "skills" / "b")
        kept, copies = dedupe_identical_skill_dirs([a, b], repo)
        assert kept == [a, b] and copies == {}

    def test_same_skill_md_but_different_reference_is_not_a_copy(self, tmp_path):
        repo = tmp_path / "repo"
        a = self._skill(repo / "skills" / "a", extra='{"v": 1}')
        b = self._skill(repo / "plugins" / "p" / "skills" / "a", extra='{"v": 2}')
        kept, copies = dedupe_identical_skill_dirs([a, b], repo)
        assert kept == [a, b] and copies == {}

    @patch("community_scan.run_batch_scan")
    @patch("community_scan.clone_repo", return_value=True)
    def test_run_community_scan_scans_once_and_reports_copies(self, _clone, mock_batch, tmp_path):
        repo = tmp_path / "skills" / "owner-repo"
        self._skill(repo / "skills" / "a")
        self._skill(repo / "plugins" / "p" / "skills" / "a")
        mock_batch.return_value = {"skills-a": {"skill_name": "skills-a", "is_safe": True, "findings_count": 0,
                                               "findings": [], "max_severity": "SAFE"}}
        skipped = {}
        results = run_community_scan("owner/repo", skills_dir=tmp_path / "skills", output_dir=tmp_path / "out",
                                     skipped_copies=skipped)
        assert [r["skill_name"] for r in results] == ["skills-a"]
        assert set(mock_batch.call_args.kwargs["names"].values()) == {"skills-a"}
        assert skipped == {"plugins/p/skills/a": "skills/a"}
        comment = format_results_comment("owner/repo", results, skipped)
        assert "Skipped 1 byte-identical copies of 1 skill(s)" in comment
        assert "`plugins/p/skills/a` → `skills/a`" in comment


# --- second scanner (NVIDIA SkillSpector) ---


def _row(stem, recommendation="SAFE", score=0):
    return {"name": f"{stem}-skillspector", "score": score, "severity": "LOW", "recommendation": recommendation, "issues": 0}


def _cisco(name, safe=True):
    return {"skill_name": name, "is_safe": safe, "findings_count": 0 if safe else 1, "findings": [],
            "max_severity": "SAFE" if safe else "HIGH"}


class TestRunSecondScanner:
    def _names(self, tmp_path, n=2):
        names = {}
        for i in range(n):
            d = tmp_path / "repo" / "skills" / f"s{i}"
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text("# s")
            names[d] = f"skills-s{i}"
        return names

    @patch("community_scan.scan_one")
    def test_scans_each_kept_dir_once_with_matching_paths(self, mock_scan, tmp_path):
        names = self._names(tmp_path)
        out = tmp_path / "results"
        mock_scan.side_effect = lambda exe, d, o, c: _row(o.stem[: -len("-skillspector")])
        got = run_second_scanner(names, out, skillspector="/opt/bin/skillspector")
        assert mock_scan.call_count == 2 and got["note"] is None
        for (exe, skill_dir, out_file, cisco_file), _ in [c for c in mock_scan.call_args_list]:
            stem = names[skill_dir]
            assert exe == "/opt/bin/skillspector"
            assert out_file == out / "skillspector" / f"{stem}-skillspector.json"
            assert cisco_file == out / f"{stem}-scan.json"
        assert set(got["rows"]) == {"skills-s0", "skills-s1"}
        assert got["rows"]["skills-s1"]["recommendation"] == "SAFE"

    @patch("community_scan.scan_one")
    def test_stale_output_is_unlinked_before_scan(self, mock_scan, tmp_path):
        names = self._names(tmp_path, n=1)
        out = tmp_path / "results"
        stale = out / "skillspector" / "skills-s0-skillspector.json"
        stale.parent.mkdir(parents=True)
        stale.write_text("{\"risk_assessment\": {\"recommendation\": \"SAFE\"}}")

        def fake(exe, d, o, c):
            assert not o.exists(), "stale report must be removed before SkillSpector runs"
            return {"name": o.stem, "error": "rc=2"}
        mock_scan.side_effect = fake
        got = run_second_scanner(names, out, skillspector="skillspector")
        assert got["rows"]["skills-s0"]["error"] == "rc=2"

    @patch("community_scan.scan_one", side_effect=RuntimeError("boom"))
    def test_crash_in_one_scan_becomes_an_error_row(self, _scan, tmp_path):
        names = self._names(tmp_path, n=1)
        got = run_second_scanner(names, tmp_path / "results", skillspector="skillspector")
        assert got["rows"]["skills-s0"]["error"].startswith("RuntimeError")

    @patch("community_scan.scan_one")
    @patch("community_scan.shutil.which", return_value=None)
    def test_missing_executable_fails_open(self, _which, mock_scan, tmp_path):
        got = run_second_scanner(self._names(tmp_path), tmp_path / "results")
        assert got["rows"] == {} and "not available" in got["note"]
        mock_scan.assert_not_called()
        comment = format_results_comment("o/r", [_cisco("skills-s0")], None, got)
        assert "SkillSpector was not available" in comment and "| SkillSpector |" not in comment

    @pytest.mark.parametrize("limit", [1, 3])
    @patch("community_scan.scan_one")
    def test_over_budget_repo_is_skipped_with_note(self, mock_scan, tmp_path, limit):
        names = self._names(tmp_path, n=limit + 1)
        got = run_second_scanner(names, tmp_path / "results", skillspector="skillspector", max_skills=limit)
        assert got["rows"] == {} and f"exceed the {limit}-skill budget" in got["note"]
        mock_scan.assert_not_called()

    @patch("community_scan.scan_one")
    def test_version_is_read_from_a_written_report(self, mock_scan, tmp_path):
        names = self._names(tmp_path, n=1)
        out = tmp_path / "results"

        def fake(exe, d, o, c):
            o.parent.mkdir(parents=True, exist_ok=True)
            o.write_text(json.dumps({"metadata": {"skillspector_version": "2.12.0"}, "risk_assessment": {"recommendation": "SAFE", "score": 0}}))
            return _row("skills-s0")
        mock_scan.side_effect = fake
        assert run_second_scanner(names, out, skillspector="skillspector")["version"] == "2.12.0"


class TestSecondScannerComment:
    def test_column_and_metrics_render_and_caution_zero_is_not_flagged(self):
        results = [_cisco("a"), _cisco("b"), _cisco("c", safe=False), _cisco("d")]
        second = {"version": "2.12.0", "note": None, "rows": {
            "a": _row("a", "SAFE", 0),
            "b": _row("b", "CAUTION", 0),            # fail-closed: not fully inspected
            "c": _row("c", "DO_NOT_INSTALL", 100),   # flagged
            "d": {"name": "d-skillspector", "error": "timeout"},
        }}
        comment = format_results_comment("o/r", results, None, second)
        assert "| SkillSpector flagged | 1 |" in comment
        assert "| SkillSpector not fully inspected | 1 |" in comment
        assert "| Skill | Safe | Findings | Max Severity | SkillSpector |" in comment
        assert "| a | Yes | 0 | SAFE | SAFE 0 |" in comment
        assert "| b | Yes | 0 | SAFE | CAUTION 0 |" in comment
        assert "| c | **No** | 1 | HIGH | DO_NOT_INSTALL 100 |" in comment
        assert "| d | Yes | 0 | SAFE | error |" in comment
        assert "SkillSpector 2.12.0, static mode" in comment
        assert "two-scanners-one-corpus" in comment
        # Only the recommendation and score are public; no second-scanner finding text.
        assert "issues" not in comment.lower().split("skillspector 2.12.0")[1].split("---")[0]

    def test_without_second_scanner_the_comment_is_unchanged(self, safe_scan_result):
        before = format_results_comment("o/r", [safe_scan_result], {"plugins/x": "skills/x"})
        after = format_results_comment("o/r", [safe_scan_result], {"plugins/x": "skills/x"}, None)
        assert before == after and "SkillSpector" not in before

    def test_skill_missing_from_second_rows_shows_a_dash(self):
        second = {"version": None, "note": None, "rows": {"a": _row("a")}}
        comment = format_results_comment("o/r", [_cisco("a"), _cisco("zz")], None, second)
        assert "| zz | Yes | 0 | SAFE | — |" in comment
