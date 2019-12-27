#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Controllers.ProbeController import api_routes

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)