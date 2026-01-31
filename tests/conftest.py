"""Shared test fixtures for the skill scanner pipeline."""

import json
import sys
from pathlib import Path

import pytest

# Ensure scripts/ is on the import path
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))


@pytest.fixture
def tmp_results_dir(tmp_path):
    """Create a temporary results directory."""
    results = tmp_path / "results"
    results.mkdir()
    return results


@pytest.fixture
def sample_scan_result():
    """A scan result with findings."""
    return {
        "skill_name": "test-skill",
        "skill_path": "/fake/path/test-skill",
        "skill_directory": "/fake/path/test-skill",
        "is_safe": False,
        "max_severity": "HIGH",
        "findings_count": 2,
        "findings": [
            {
                "id": "FINDING_001",
                "rule_id": "TEST_RULE_HIGH",
                "category": "command_injection",
                "severity": "HIGH",
                "title": "Test high finding",
                "description": "A test finding with high severity",
                "file_path": "test.sh",
                "line_number": 1,
                "snippet": "echo $USER_INPUT",
                "remediation": "Sanitize input",
                "analyzer": "static",
                "metadata": {},
            },
            {
                "id": "FINDING_002",
                "rule_id": "TEST_RULE_LOW",
                "category": "policy_violation",
                "severity": "LOW",
                "title": "Test low finding",
                "description": "A test finding with low severity",
                "file_path": "SKILL.md",
                "line_number": None,
                "snippet": None,
                "remediation": "Add license field",
                "analyzer": "static",
                "metadata": {},
            },
        ],
        "scan_duration_seconds": 0.01,
        "duration_ms": 10,
        "analyzers_used": ["static_analyzer", "behavioral_analyzer"],
        "timestamp": "2026-01-31T00:00:00.000000",
    }


@pytest.fixture
def safe_scan_result():
    """A clean/safe scan result."""
    return {
        "skill_name": "safe-skill",
        "skill_path": "/fake/path/safe-skill",
        "is_safe": True,
        "max_severity": "SAFE",
        "findings_count": 0,
        "findings": [],
        "analyzers_used": ["static_analyzer"],
        "timestamp": "2026-01-31T00:00:00.000000",
    }


@pytest.fixture
def sample_skill_list():
    """A list of skill dicts as returned by fetch_top_skills()."""
    return [
        {
            "rank": 1,
            "name": "skill-alpha",
            "id": "skill-alpha",
            "repo": "owner/repo-a",
            "installs": 1000,
            "source": "skills.sh",
        },
        {
            "rank": 2,
            "name": "skill-beta",
            "id": "skill-beta",
            "repo": "owner/repo-a",
            "installs": 500,
            "source": "skills.sh",
        },
        {
            "rank": 3,
            "name": "skill-gamma",
            "id": "gamma-slug",
            "repo": None,
            "installs": 200,
            "source": "clawhub",
        },
    ]
