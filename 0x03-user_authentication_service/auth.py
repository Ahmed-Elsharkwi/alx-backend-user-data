#!/usr/bin/env python3
"""
auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hashing the password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
