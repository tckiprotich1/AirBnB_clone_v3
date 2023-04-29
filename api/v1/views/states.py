#!/usr/bin/python3
""" State objects that handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ Retrieves the list of all State objects """
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())
    return jsonify(states)