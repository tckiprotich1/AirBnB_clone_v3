#!/usr/bin/python3
""" Module for index.py """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns a JSON """
    return jsonify({"status": "OK"})

# Route: /api/v1/stats
@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Returns a JSON """
    from models import storage
    classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
               "Review": "reviews", "State": "states", "User": "users"}
    for key, value in classes.items():
        classes[key] = storage.count(key)
    return jsonify(classes)
