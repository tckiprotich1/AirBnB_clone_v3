#!/usr/bin/python3
""" Module for __init.py__ """

from flask import Flask, Blueprint, jsonify


"""
# create a variable app_views which is an instance of
 Blueprint (url prefix must be /api/v1)
"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
# imports states
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *