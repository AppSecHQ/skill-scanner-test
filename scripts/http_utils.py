"""Shared HTTP utilities with retry support."""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


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
