from app import db

class Probe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))