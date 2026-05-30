import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["300 per minute"],
    # Use Redis when available (required for multi-worker Gunicorn); fall back to in-process memory
    storage_uri=os.environ.get("REDIS_URL", "memory://"),
    # Fail open: if Redis is unreachable, skip limiting rather than crashing every request
    swallow_errors=True,
)
