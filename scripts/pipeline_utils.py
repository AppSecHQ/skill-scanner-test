"""Shared pipeline utilities: HTTP sessions, logging constants."""

import atexit

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

LOG_FORMAT = "%(asctime)s [%(levelname)-7s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

_session: requests.Session | None = None


def get_retry_session(
    retries: int = 3,
    backoff_factor: float = 0.5,
    status_forcelist: tuple[int, ...] = (500, 502, 503, 504),
) -> requests.Session:
    """
    Create a requests Session with automatic retry on transient failures.

    Args:
        retries: Maximum number of retries per request
        backoff_factor: Delay multiplier between retries (0.5 -> 0.5s, 1s, 2s)
        status_forcelist: HTTP status codes that trigger a retry

    Returns:
        Configured requests.Session
    """
    session = requests.Session()
    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=list(status_forcelist),
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def get_session() -> requests.Session:
    """Return the shared retry-enabled session, creating it on first call."""
    global _session
    if _session is None:
        _session = get_retry_session()
    return _session


def close_session() -> None:
    """Close the shared session if open. Safe to call multiple times."""
    global _session
    if _session is not None:
        _session.close()
        _session = None


atexit.register(close_session)
