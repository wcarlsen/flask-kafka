from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON

db = SQLAlchemy()


class MessageLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(JSON)
    timestamp = db.Column(TIMESTAMP)
