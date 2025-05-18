from flask import request, jsonify
from takehome_api.src.models.Provider import Provider
from takehome_api.src.models.associations import State, Insurance
from takehome_api.src.database import db


def add_provider():
    data = request.get_json()
    provider_data = data.get("provider", {})
    provider_name = provider_data.get("name")
    state_codes = provider_data.get("states", [])
    insurance_names = provider_data.get("insurances", [])

    # validate input
    if not all([provider_name, state_codes, insurance_names]):
        return jsonify({"error": "Missing provider information"}), 400

    # query for state and insurance objects
    state_objs = []
    for code in state_codes:
        state = State.query.filter_by(code=code).first()
        if not state:
            state = State(code=code)
            db.session.add(state)
            db.session.flush()  # ensures state gets an id before association
        state_objs.append(state)

    insurance_objs = []
    for name in insurance_names:
        insurance = Insurance.query.filter_by(name=name).first()
        if not insurance:
            insurance = Insurance(name=name)
            db.session.add(insurance)
            db.session.flush()  # ensures insurance gets an id before association
        insurance_objs.append(insurance)

    provider = Provider(name=provider_name)
    provider.states.extend(state_objs)
    provider.insurances.extend(insurance_objs)

    db.session.add(provider)
    db.session.commit()

    return (
        jsonify(
            {
                "name": provider_name,
                "states": [s.code for s in state_objs],
                "insurances": [i.name for i in insurance_objs],
            }
        ),
        201,
    )
