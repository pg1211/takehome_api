from takehome_api.src.models.Appointment import Appointment
from flask import jsonify


def list_appointments():
    appointments = Appointment.query.all()
    return jsonify(
        [
            {
                "id": a.id,
                "patient": a.patient,
                "scheduled": a.scheduled,
                "appointment_id": a.appointment_id,
                "provider": a.provider,
                "time": a.time,
            }
            for a in appointments
        ]
    )
