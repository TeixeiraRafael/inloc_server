from app import db
from sqlalchemy.dialects import mysql
class Probe(db.Model):
    id = db.Column(mysql.INTEGER, primary_key=True)
    address1 = db.Column(mysql.VARCHAR(length=17))
    address2 = db.Column(mysql.VARCHAR(length=17))
    rssi = db.Column(mysql.INTEGER)
    payload_name = db.Column(mysql.TEXT)
    timestamp = db.Column(mysql.TIMESTAMP)
    time_offset = db.Column(mysql.VARCHAR(length=6))
    station = db.Column(mysql.TEXT)

    def get_all():
        pass