from flask import request, jsonify
from takehome_api.src.models.Provider import Provider
from takehome_api.src.database import db


def add_provider():
    data = request.get_json()
    provider_data = data.get("provider", {})
    name = provider_data.get("name")
    states = provider_data.get("states")
    insurances = provider_data.get("insurances")

    # Validate input
    if not all([name, states, insurances]):
        return jsonify({"error": "Missing patient information"}), 400

    provider = Provider(name=name)
    db.session.add(provider)
    db.session.commit()

    return (
        jsonify(
            {
                "name": name,
                "states": states,
                "insurances": insurances
            }
        ),
        201,
    )

    pass
