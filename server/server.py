import os
import sys
import logging
import structlog
from app import create_app
from app.service import start_consumer_service
from app.models import db

logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
structlog.configure(
    processors=[structlog.processors.JSONRenderer(indent=1, sort_keys=True)],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
)

app = create_app(os.getenv("ENVIRONMENT") or "default")
start_consumer_service(app, db)