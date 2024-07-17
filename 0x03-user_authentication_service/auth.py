#!/usr/bin/env python3
"""
auth module
"""
import bcrypt


def _hash_password(password):
    """ hashing the password """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    print(salt)
    return (bcrypt.hashpw(bytes, salt))
