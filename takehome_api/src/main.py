from dotenv import load_dotenv

load_dotenv(verbose=True)
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from instance.config import APP_CONFIG
from takehome_api.src.database import db

from takehome_api.src.models.Provider import Provider
from takehome_api.src.models.Patient import Patient
from takehome_api.src.models.Appointment import Appointment
from takehome_api.src.external import schedule_with_provider

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(APP_CONFIG[config_name])
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return str(Response.default_status) + " OK"

    # TODO:
    # Add an appointment endpoint

    return app
