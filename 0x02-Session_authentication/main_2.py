#!/usr/bin/python3
""" Check response
"""
import requests

if __name__ == "__main__":
    r = requests.get('http://0.0.0.0:3456/api/v1/users/me', cookies={'_my_session_id': "fake session ID"})
    if r.status_code != 403:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    print("OK", end="")

