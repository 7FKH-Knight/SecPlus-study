import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Use Redis if REDIS_URL is set AND the redis package is installed.
# Fall back to in-process memory (safe for single-worker Gunicorn).
_redis_url = os.environ.get("REDIS_URL")
if _redis_url:
    try:
        import redis as _redis_check  # noqa: F401
        _storage_uri = _redis_url
    except ImportError:
        _storage_uri = "memory://"
else:
    _storage_uri = "memory://"

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["300 per minute"],
    storage_uri=_storage_uri,
    swallow_errors=True,
)
