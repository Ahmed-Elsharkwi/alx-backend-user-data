#!/usr/bin/env python3
"""
module of session auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ session Auth """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session """
        if user_id is None or type(user_id) is not str:
            return None

        id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return user id based on the session_id """
        if session_id is None or type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
