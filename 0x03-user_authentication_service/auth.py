#!/usr/bin/env python3
"""
auth module
"""
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register new user """
        password = _hash_password(password)
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound or InvalidRequestError:
            user = self._db.add_user(email, password)
        return user


def _hash_password(password: str) -> bytes:
    """
    hashing the password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
