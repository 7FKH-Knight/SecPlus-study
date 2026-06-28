import logging
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

logger = logging.getLogger(__name__)


def _resolve_storage_uri():
    """Use Redis only if REDIS_URL is set AND actually reachable.

    A REDIS_URL that's set but unreachable previously caused every
    limiter check to throw, and swallow_errors=True silently let all
    requests through unthrottled. Probing the connection at startup
    means a broken Redis falls back to the safe in-process store
    instead of disabling rate limiting app-wide.
    """
    redis_url = os.environ.get("REDIS_URL")
    if not redis_url:
        return "memory://"
    try:
        import redis
        redis.from_url(redis_url, socket_connect_timeout=2).ping()
        return redis_url
    except Exception:
        logger.warning("REDIS_URL is set but unreachable; falling back to in-process rate-limit storage")
        return "memory://"


_storage_uri = _resolve_storage_uri()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["300 per minute"],
    storage_uri=_storage_uri,
    swallow_errors=True,
)
