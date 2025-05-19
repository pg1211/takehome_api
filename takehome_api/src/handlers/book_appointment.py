from flask import request, jsonify
from takehome_api.src.models.Provider import Provider
from takehome_api.src.external import schedule_with_provider
from takehome_api.src.models.Patient import Patient
from takehome_api.src.models.Appointment import Appointment
from takehome_api.src.database import db


# book an appointment for a patient if there is a matching provider
def book_appointment():
    data = request.get_json() or {}
    patient_data = data.get("patient", {})
    name = patient_data.get("name")
    email = patient_data.get("email")
    state = patient_data.get("state")
    insurance = patient_data.get("insurance")

    # validate input
    if not all([name, email, state, insurance]):
        return jsonify({"error": "Missing patient information"}), 400

    # find a provider licensed in the state and accepting the insurance
    provider = (
        Provider.query.filter(Provider.states.any(code=state))
        .filter(Provider.insurances.any(name=insurance))
        .first()
    )
    if not provider:
        return jsonify({"error": "No matching provider found"}), 404

    # simulate scheduling
    scheduling_result = schedule_with_provider(provider, name)

    # add patient and appt to db
    patient = Patient(name=name, email=email, state=state, insurance=insurance)
    db.session.add(patient)
    db.session.commit()

    appointment = Appointment(
        patient=name,
        scheduled=scheduling_result["scheduled"],
        appointment_id=scheduling_result["appointment_id"],
        provider=provider.name,
        time=scheduling_result["time"],
    )
    db.session.add(appointment)
    db.session.commit()

    # return response
    response = {
        "patient": name,
        "scheduled": scheduling_result["scheduled"],
        "appointment_id": scheduling_result["appointment_id"],
        "provider": provider.name,
        "time": scheduling_result["time"],
    }
    return jsonify(response), 201
