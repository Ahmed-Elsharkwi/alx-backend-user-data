#!/usr/bin/env python3
"""
auth module
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
