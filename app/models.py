from app import db

class Flight(db.Model):
        origin = db.Column(db.String(50), nullable=False)
        destination = db.Column(db.String(50), nullable=False)
        takeoff = db.Column(db.DateTime)
        landing = db.Column(db.DateTime)
        date = db.Column(db.DateTime)
        model = db.Column(db.String(50))
        price = db.Column(db.Float)
        airline = db.Column(db.String(50), nullable=False)
        id = db.Column(db.Integer, primary_key=True)

