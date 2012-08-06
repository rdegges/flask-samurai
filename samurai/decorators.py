"""Useful decorators and stuff."""


from functools import wraps

from basicauth import DecodeError, decode
from flask import abort, current_app, request


def heroku(f):
    """Validate that all incoming requests are coming from Heroku.

    If any request is invalid (can't prove it is the Heroku origin server),
    raise a 401.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            username, password = decode(request.headers['AUTHORIZATION'])
        except (DecodeError, KeyError):
            abort(401)

        if (username != current_app.config.get('SAMURAI_USERNAME') or
                password != current_app.config.get('SAMURAI_PASSWORD')):
            abort(401)

        return f(*args, **kwargs)

    return decorated_function
