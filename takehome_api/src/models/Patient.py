from takehome_api.src.database import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    insurance = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, state, insurance):
        self.name = name
        self.email = email
        self.state = state
        self.insurance = insurance
