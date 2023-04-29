#!/usr/bin/python3
""" Module for app.py """
from flask import Flask, Blueprint, jsonify
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
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
