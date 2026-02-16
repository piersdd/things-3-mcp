"""API key authentication for HTTP transport.

When running in HTTP mode, requires X-API-Key header (or api_key query param).
Generates a strong random key on first run if THINGS_MCP_API_KEY is not set.
"""

from __future__ import annotations

import logging
import os
import secrets

logger = logging.getLogger(__name__)

_API_KEY: str | None = None


def get_api_key() -> str:
    """Get or generate the API key for HTTP transport."""
    global _API_KEY  # noqa: PLW0603
    if _API_KEY is not None:
        return _API_KEY

    key = os.environ.get("THINGS_MCP_API_KEY")
    if key:
        _API_KEY = key
        return _API_KEY

    # Generate a strong random key
    _API_KEY = secrets.token_urlsafe(32)
    logger.warning(
        "No THINGS_MCP_API_KEY set — generated temporary key: %s\n"
        "Set THINGS_MCP_API_KEY env var to persist this key.",
        _API_KEY,
    )
    return _API_KEY


def validate_api_key(provided_key: str | None) -> bool:
    """Validate an API key against the configured key."""
    if not provided_key:
        return False
    return secrets.compare_digest(provided_key, get_api_key())
