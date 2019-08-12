from flask import Flask
from flask_migrate import Migrate
from flask_prom import monitor
from healthcheck import HealthCheck
from structlog import get_logger
from config import config
from app.models import db

migrate = Migrate()


def create_app(configuration):


    logger = get_logger()

    logger.info("Initialising app")
    app = Flask(__name__)

    logger.info("Load config")
    app.config.from_object(config[configuration])

    logger.info("Initialising db")
    db.init_app(app)

    logger.info("Initialise migration")
    migrate.init_app(
        app,
        db
    )

    logger.info("Initialise metrics endpoint")
    monitor(app, path="/metrics", http_server=True, port=8080, addr="127.0.0.1")

    logger.info("Initialise health endpoint")
    health = HealthCheck(app, "/healthz")

    logger.info("App running")
    return app
