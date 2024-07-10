#!/usr/bin/env python3
"""
auth module
"""
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ inherits from Auth
    """
