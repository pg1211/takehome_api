from dotenv import load_dotenv
from flask import Flask, Response
from flask_cors import CORS
from instance.config import APP_CONFIG
from takehome_api.src.database import db
# handling functions
from takehome_api.src.handlers.book_appointment import book_appointment
from takehome_api.src.handlers.list_appointments import list_appointments

load_dotenv(verbose=True)


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
    @app.route("/appointment", methods=["POST"])
    def appointment_route():
        return book_appointment()

    # for viewing appointments in the future
    @app.route("/appointments", methods=["GET"])
    def appointments_route():
        return list_appointments()

    @app.route("/providers", methods=["POST"])
    def providers_route():
        return str(Response.default_status) + " OK"

    return app
