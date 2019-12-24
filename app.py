#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Controllers.ProbeController import bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()