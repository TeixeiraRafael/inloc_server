from app import db
from sqlalchemy.dialects import mysql
from datetime import datetime

class State(db.Model):
    id = db.Column(mysql.INTEGER, primary_key=True)
    station_id = db.Column(mysql.TEXT)
    mode = db.Column(mysql.TEXT)
    channel = db.Column(mysql.TEXT)
    last_seen = db.Column(mysql.DATETIME)
    
    def as_json(self):
        json = {
            "id": self.id,
            "station_id": self.station_id,
            "mode": self.mode,
            "channel": self.channel,
            "last_seen": str(self.last_seen),
        }
        return json