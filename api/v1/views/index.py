#!/bin/usr/python3
""" Module for index.py """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns a JSON """
    return jsonify({"status": "OK"})
