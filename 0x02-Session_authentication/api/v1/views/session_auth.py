#!/usr/bin/env python3
""" module of all the authincation routes """
from api.v1.views import app_views
from os import getenv
from flask import abort, jsonify, request, redirect
from models.user import User


@app_views.route("/auth_session/login", methods=['POST'], strict_slashes=False)
def authicate():
    """ authicante the login """
    email_1 = request.form.get('email')
    if email_1 is None or len(email_1.strip()) == 0:
        return jsonify({"error": "email_missing"}), 400

    pwd_1 = request.form.get('password')
    if pwd_1 is None or len(pwd_1.strip()) == 0:
        return jsonify({"error": "password_missing"}), 400

    try:
        new_list = User.search({'email': email_1})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if len(new_list) <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    res = new_list[0].is_valid_password(pwd_1)
    if res is False:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(new_list[0].id)
    user_dict = jsonify(new_list[0].to_json())
    user_dict.set_cookie(getenv("SESSION_NAME"), session_id)
    return user_dict
