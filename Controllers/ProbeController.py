from flask import Flask, Blueprint, request, jsonify
import json

api_routes = Blueprint('api', __name__)

from Models.Probe import *

@api_routes.route('/probe', methods=['GET'])
def get_all():
    query = db.session.query(Probe)
    response = query.all()
    result = []

    for r in response:
        encoded_result = {
            "id": r.id,
            "address1": r.address1,
            "address2": r.address2,
            "rssi": r.rssi,
            "payload_name": r.payload_name,
            "timestamp": r.timestamp,
            "time_offset": r.time_offset,
            "station": r.station   
        }
        result.append(encoded_result)

    return jsonify(result)

@api_routes.route('/probe/count', methods=['GET'])
def get_count():
    query = db.session.query(Probe)
    response = len(query.all())    
    return jsonify(response)

@api_routes.route('/probe', methods=['POST'])
def insert_probe():
    request_body = request.get_json()
    probe = Probe()

    probe.address1 = request_body['address_1']
    probe.address2 = request_body['address_2']
    probe.rssi = request_body['rssi']
    probe.payload_name = request_body['payload_name']

    #splitting timestamp and timezone with list operators
    probe.timestamp = request_body['timestamp'][0:-7]
    probe.time_offset = request_body['timestamp'][-6:]

    probe.station = request_body['station']
    db.session.add(probe)
    db.session.commit()

    return ("OK")