"""This module contains the auth endpoint routes"""

#blueprint make make our modules like miny apps
from flask import jsonify, Blueprint

AUTH = Blueprint('AUTH', __name__)

@AUTH.route('/')
def home():
  """
    This is the default method
  """
  return jsonify({'message': 'Hello World!'}), 200