#!/usr/bin/env python3
""" module of all the authincation routes """
from api.v1.views import app_views
from flask import abort, jsonify, request, redirect
from models.user import User


@app_view.route("auth_session/login", method=['POST'], strict_slaches=False)
def authicate():
    """ authicante the login """
    email_1 = request.form.get('email')
    if email_1 is None or email_1 == '':
        return jsonify({"error": "email_missing"}, 400)

    pwd_1 - request.form.get('password')
    if pwd_1 is None or pwd_1 == '':
        return jsonify({"error": "password_missing"}, 400)

