from flask import Flask, request
from .extensions import api
from flask_restx import namespace
from app.controllers.Detect import Detect_ns

def create_app(config_file="config.py"):
    app = Flask(__name__)    
    app.config.from_pyfile(config_file)
    print(app.config)
    api.init_app(app)
    api.add_namespace(Detect_ns)

    return app