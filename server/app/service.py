import threading
from confluent_kafka import Consumer, KafkaError
import datetime
from structlog import get_logger
from app.models import MessageLog
import asyncio

logger = get_logger()

c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)
c.subscribe(["test"])


def consumer_service(app, db):
    logger.info("Consumer service started")
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            logging.info("consuming_error", msg="Consumer error: {}".format(msg.error()))
            continue
        logger.info("consuming_msg", payload=msg.value().decode("utf-8"), offset=msg.offset(), partition=msg.partition(), timestamp_producer=msg.timestamp(), timestamp_consumer=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        with app.app_context():
            message = MessageLog(
                msg=msg.value().decode("utf-8"), timestamp=datetime.datetime.utcnow()
            )
            db.session.add(message)
            db.session.commit()


def start_consumer_service(app, db):
    thread = threading.Thread(target=consumer_service, args=[app, db])
    thread.setDaemon(True)
    thread.start()