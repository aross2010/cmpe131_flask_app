from app import db
from sqlalchemy import Numeric


class Flight(db.Model):
        origin = db.Column(db.String(50), nullable=False)
        destination = db.Column(db.String(50), nullable=False)
        takeoff = db.Column(db.DateTime)
        landing = db.Column(db.DateTime)
        originDate = db.Column(db.Date)
        destinationDate = db.Column(db.Date)
        model = db.Column(db.String(50))
        price = db.Column(db.Integer)
        airline = db.Column(db.String(50), nullable=False)
        id = db.Column(db.Integer, primary_key=True)
        class_type = db.Column(db.String(50))

