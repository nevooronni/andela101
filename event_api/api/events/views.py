"""This is module is where we initailize the app"""

from flask import flask

APP = Flask(__name__)

from event_api.api.auth.views import AUTH
APP.register_blueprint(AUTH)