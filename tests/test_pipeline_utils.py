"""Tests for scripts/pipeline_utils.py"""

import requests

from pipeline_utils import get_retry_session, get_session, close_session
import pipeline_utils


class TestGetRetrySession:
    def test_returns_session(self):
        session = get_retry_session()
        assert isinstance(session, requests.Session)
        session.close()

    def test_returns_new_session_each_call(self):
        s1 = get_retry_session()
        s2 = get_retry_session()
        assert s1 is not s2
        s1.close()
        s2.close()

    def test_retry_adapter_mounted(self):
        session = get_retry_session()
        adapter = session.get_adapter("https://example.com")
        assert adapter.max_retries.total == 3
        session.close()

    def test_custom_retries(self):
        session = get_retry_session(retries=5)
        adapter = session.get_adapter("https://example.com")
        assert adapter.max_retries.total == 5
        session.close()

    def test_custom_backoff(self):
        session = get_retry_session(backoff_factor=1.0)
        adapter = session.get_adapter("https://example.com")
        assert adapter.max_retries.backoff_factor == 1.0
        session.close()

    def test_custom_status_forcelist(self):
        session = get_retry_session(status_forcelist=(429, 500))
        adapter = session.get_adapter("https://example.com")
        assert 429 in adapter.max_retries.status_forcelist
        assert 500 in adapter.max_retries.status_forcelist
        session.close()

    def test_only_get_allowed(self):
        session = get_retry_session()
        adapter = session.get_adapter("https://example.com")
        assert adapter.max_retries.allowed_methods == ["GET"]
        session.close()


class TestGetSession:
    def setup_method(self):
        close_session()

    def teardown_method(self):
        close_session()

    def test_returns_session(self):
        session = get_session()
        assert isinstance(session, requests.Session)

    def test_returns_same_instance(self):
        s1 = get_session()
        s2 = get_session()
        assert s1 is s2

    def test_creates_new_after_close(self):
        s1 = get_session()
        close_session()
        s2 = get_session()
        assert s1 is not s2


class TestCloseSession:
    def setup_method(self):
        close_session()

    def test_close_when_none(self):
        close_session()  # should not raise

    def test_close_resets_to_none(self):
        get_session()
        close_session()
        assert pipeline_utils._session is None

    def test_double_close(self):
        get_session()
        close_session()
        close_session()  # should not raise
        assert pipeline_utils._session is None
