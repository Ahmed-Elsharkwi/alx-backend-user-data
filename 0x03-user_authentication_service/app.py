#!/usr/bin/env python3
"""
app module
"""
from flask import Flask, jsonify, request
from auth import Auth


Auth = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def reload():
    """ reload something """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', strict_slashes=False, methods=['POST'])
def regiserter_user():
    """ register users """
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
