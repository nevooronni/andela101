"""This is entry point for app"""
from flask import flask

App = Flask(__name__)

from event_api.api.auth.views import AUTH