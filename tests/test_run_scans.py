"""Tests for scripts/run_scans.py"""

import io
import zipfile
from pathlib import Path

import pytest

from run_scans import (
    sanitize_filename,
    parse_repo_arg,
    repo_to_dirname,
    find_skill_path,
    safe_extract,
    get_unique_repos,
)


class TestSanitizeFilename:
    def test_basic_name(self):
        assert sanitize_filename("my-skill") == "my-skill"

    def test_spaces_to_dashes(self):
        assert sanitize_filename("My Skill Name") == "my-skill-name"

    def test_special_characters_removed(self):
        assert sanitize_filename("My Skill (v2)") == "my-skill--v2"

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
    def _make_zip(self, members: dict[str, str]) -> zipfile.ZipFile:
        """Create an in-memory ZIP with given filename->content pairs."""
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            for name, content in members.items():
                zf.writestr(name, content)
        buf.seek(0)
        return zipfile.ZipFile(buf, "r")

    def test_safe_zip_extracts(self, tmp_path):
        zf = self._make_zip({"hello.txt": "world", "sub/file.txt": "nested"})
        safe_extract(zf, tmp_path)
        assert (tmp_path / "hello.txt").read_text() == "world"
        assert (tmp_path / "sub" / "file.txt").read_text() == "nested"

    def test_path_traversal_blocked(self, tmp_path):
        """A ZIP with ../evil.txt must be rejected."""
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr("../evil.txt", "malicious content")
        buf.seek(0)
        zf = zipfile.ZipFile(buf, "r")

        with pytest.raises(ValueError, match="path traversal"):
            safe_extract(zf, tmp_path)

        # Verify nothing was extracted
        assert not (tmp_path.parent / "evil.txt").exists()

    def test_deeply_nested_traversal_blocked(self, tmp_path):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr("foo/../../evil.txt", "malicious")
        buf.seek(0)
        zf = zipfile.ZipFile(buf, "r")

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
