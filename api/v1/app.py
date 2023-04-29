#!/usr/bin/python3

""" Module for app.py
    This module creates an instance of Flask
 """
from flask import Flask, Blueprint, jsonify
import os
from models import storage
# importing app_views from api.v1.views
from api.v1.views import app_views

app = Flask(__name__)

# registering blueprint
app.register_blueprint(app_views)
"""
# declare a method to handle @app.teardown_appcontext
 that calls storage.close()"""


@app.teardown_appcontext
def teardown_appcontext(self):
    """ Method to handle teardown """
    storage.close()


# declare a method to handle 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """ Method to handle 404 errors """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
