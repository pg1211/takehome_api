from takehome_api.src.models.Provider import Provider
from flask import jsonify


def list_providers():
    providers = Provider.query.all()
    return jsonify(
        [
            {
                "id": p.id,
                "name": p.name,
                "states": [state.name for state in p.states],
                "insurances": [ins.name for ins in p.insurances],
            }
            for p in providers
        ]
    )
