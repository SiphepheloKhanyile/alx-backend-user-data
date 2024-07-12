#!/usr/bin/env python3
"""
Route module for the API
"""
import os  # pylint: disable=W0611
from os import getenv
from flask import Flask, jsonify, abort, request  # pylint: disable=W0611
from flask_cors import (CORS, cross_origin)  # pylint: disable=W0611
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    # print(error)
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """401 Unauthorized handler
    Args:
        error (_type_): _description_
    Returns:
        str: _description_
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port))
