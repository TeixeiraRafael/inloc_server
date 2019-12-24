from flask import Flask, Blueprint, request, jsonify

api_routes = Blueprint('api', __name__)

from Models.Probe import *

@api_routes.route('/probe', methods=['GET'])
def get_all():
    response = {
        'Name': 'Rafael',
        'Age' : 22
    }
    return(jsonify(response))

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