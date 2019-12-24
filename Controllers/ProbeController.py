from flask import Flask, Blueprint

bp = Blueprint('api', __name__)

from Models.Probe import *

@bp.route('/probe', methods=['GET'])
def get_all():
    return(str(Probe()))