from flask import Flask, Blueprint, request, jsonify
import json

api_routes = Blueprint('api', __name__)

from Models.Probe import *

@api_routes.route('/probe', methods=['GET'])
def get_all():
    query = db.session.query(Probe)
    probes = query.all()
    result = []

    for probe in probes:
        result.append(probe.as_json())

    return jsonify(result)

@api_routes.route('/probe/<address_2>', methods=['GET'])
def get_by_mac(address_2):
    query = db.session.query(Probe).filter(Probe.address2.like(address_2))
    probes = query.all()
    response = []
    for probe in probes:
        response.append(probe.as_json())
    return jsonify(response)


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

    return ("OK", 200)