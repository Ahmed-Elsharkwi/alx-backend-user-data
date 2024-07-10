#!/usr/bin/env python3
"""
auth module
"""
import base64
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract_base64 """
        if (authorization_header is None) or (type(
                authorization_header) != str):
            return None

        new_list = authorization_header.split(" ")
        if new_list[0] != "Basic":
            return None

        return new_list[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode text """
        text = base64_authorization_header

        if text is None or type(text) is not str:
            return None

        try:
            text = base64.b64decode(text)
            return text.decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ return the email and the password of the user """
        text = decoded_base64_authorization_header

        if text is None or type(text) is not str or ':' not in text:
            return (None, None)

        new_list = text.split(':')
        return (new_list[0], new_list[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ return user instance """
        if user_email is None or type(
                user_email) is not str or user_pwd is None or type(
                        user_pwd) is not str:
            return None
        try:
            new_list = User.search({'email': user_email})
        except Exception:
            return None
        if len(new_list) <= 0:
            return None
        res = new_list[0].is_valid_password(user_pwd)
        if res:
            return new_list[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return a User instance """
        header = self.authorization_header(request)
        encoded_text = self.extract_base64_authorization_header(header)
        decoded_text = self.decode_base64_authorization_header(encoded_text)
        user_data = self.extract_user_credentials(decoded_text)
        return self.user_object_from_credentials(user_data)
