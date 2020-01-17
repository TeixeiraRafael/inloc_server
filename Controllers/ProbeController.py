from flask import Flask, Blueprint, request, jsonify
import json
from scapy.all import *

import codecs

api_routes = Blueprint('api', __name__)
packet_classes = {c.__name__: c for c in scapy.packet.Packet.__subclasses__()}

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
    
    recvd_type_name = request_body['packet_type']
    recvd_raw_packet_data = request_body['raw_packet_data']

    raw_pkt = codecs.decode(recvd_raw_packet_data.encode(), "base64")

    try:
        pkt = packet_classes[recvd_type_name](raw_pkt)
        pkt.show()
        return "ohdamn"
    
    except KeyError:
        return "Invalid packet type!"
    
