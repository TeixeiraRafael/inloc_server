from app import db
from sqlalchemy.dialects import mysql
from datetime import datetime

class Probe(db.Model):
    id = db.Column(mysql.INTEGER, primary_key=True)
    address1 = db.Column(mysql.VARCHAR(length=17))
    address2 = db.Column(mysql.VARCHAR(length=17))
    rssi = db.Column(mysql.INTEGER)
    payload_name = db.Column(mysql.TEXT)
    timestamp = db.Column(mysql.DATETIME)
    time_offset = db.Column(mysql.VARCHAR(length=6))
    station = db.Column(mysql.TEXT)
    
    def as_json(self):
        json = {
            "id": self.id,
            "address_1": self.address1,
            "address_2": self.address2,
            "rssi": self.rssi,
            "payload_name": self.payload_name,
            "timestamp": str(self.timestamp),
            "time_offset": self.time_offset,
            "station": self.station
        }
        return json