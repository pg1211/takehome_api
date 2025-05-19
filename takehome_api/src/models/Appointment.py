from takehome_api.src.database import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # added fields to match appointment output
    patient = db.Column(db.String(200), nullable=False)
    scheduled = db.Column(db.Boolean, nullable=False)
    appointment_id = db.Column(db.String(100), nullable=False)
    provider = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(27), nullable=False)

    def __init__(self, patient, scheduled, appointment_id, provider, time):
        self.patient = patient
        self.scheduled = scheduled
        self.appointment_id = appointment_id
        self.provider = provider
        self.time = time
