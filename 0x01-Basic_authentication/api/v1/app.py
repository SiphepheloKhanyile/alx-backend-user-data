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

auth = None
# auth = getenv("AUTH_TYPE")

# if auth is not None:

if getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error):  # -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """
    401 error Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """
    403 error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def filtering():
    """
    Filter requests
    """
    if auth is None:
        return

    check_list = ['/api/v1/status/', '/api/v1/unauthorized/',
                  '/api/v1/forbidden/']

    if auth.require_auth(request.path, check_list) is not True:
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port))
