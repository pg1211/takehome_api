from takehome_api.src.database import db
from takehome_api.src.models.associations import provider_states, provider_insurances

# from takehome_api.src.models.associations import State, Insurance


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # add additional fields as needed
    states = db.relationship(
        "State", secondary=provider_states, backref="licensed_providers", lazy="dynamic"
    )

    insurances = db.relationship(
        "Insurance",
        secondary=provider_insurances,
        backref="accepted_providers",
        lazy="dynamic",
    )

    def __init__(self, name, states=None, insurances=None):
        self.name = name
        if states:
            self.states = states
        if insurances:
            self.insurances = insurances
