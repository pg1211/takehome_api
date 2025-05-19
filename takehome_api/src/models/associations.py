from takehome_api.src.database import db

"""
these tables will be used to create many to many relationships between:
- providers and states
- providers and insurances
"""

provider_states = db.Table(
    "provider_states",
    db.Column(
        "provider_id", db.Integer, db.ForeignKey("provider.id"), primary_key=True
    ),
    db.Column("state", db.String(2), db.ForeignKey("state.code"), primary_key=True),
)

provider_insurances = db.Table(
    "provider_insurances",
    db.Column(
        "provider_id", db.Integer, db.ForeignKey("provider.id"), primary_key=True
    ),
    db.Column(
        "insurance", db.String(100), db.ForeignKey("insurance.name"), primary_key=True
    ),
)


class State(db.Model):
    __tablename__ = "state"
    code = db.Column(db.String(2), primary_key=True)

    def __init__(self, code):
        self.code = code


class Insurance(db.Model):
    __tablename__ = "insurance"
    name = db.Column(db.String(100), primary_key=True)

    def __init__(self, name):
        self.name = name
