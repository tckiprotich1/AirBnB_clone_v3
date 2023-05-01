#!/usr/bin/python3
"""
a new view for Amenity objects that handles all default RESTFul API actions:
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/amenities', methods=[GET], strict_slashes=False)
def get_amenities():
    amenities = [Amenity.to_dict() for Amenity in storage.all
                 ("Amenity").values()]
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=[GET],
                 strict_slashes=False)
def get_amenity(amenity_id):
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
        return jsonify(amenity.to_dict)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    ignore_keys = ['id', 'created_at', 'updated_at']
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
