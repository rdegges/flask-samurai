"""Useful decorators and stuff."""


from functools import wraps
from os import environ

from basicauth import DecodeError, decode
from flask import abort, request


def heroku(f):
    """Validate that all incoming requests are coming from Heroku.

    If any request is invalid (can't prove it is the Heroku origin server),
    raise a 401.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        authorization = request.headers.get('AUTHORIZATION')
        if not authorization:
            abort(401)

        try:
            username, password = decode(request.headers['AUTHORIZATION'])
        except DecodeError:
            abort(401)

        if username != environ.get('SAMURAI_USERNAME') or password != environ.get('SAMURAI_PASSWORD'):
            abort(401)

        return f(*args, **kwargs)

    return decorated_function
