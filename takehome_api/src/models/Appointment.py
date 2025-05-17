from takehome_api.src.database import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(200), nullable=False)
    scheduled = db.Column(db.Boolean, nullable=False)
    appointment_id = db.Column(db.String(100), nullable=False)
    provider = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(27), nullable=False)
