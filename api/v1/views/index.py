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
def count():
    '''retrieves the number of each objects by type'''
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)

