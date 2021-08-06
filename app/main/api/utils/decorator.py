import functools
from flask import request


def debug(func):

    @functools.wraps(func)
    def wrapper_debugger(*args, **kwargs):
        print(request.data)
        value = func(*args, **kwargs)
        return value
    return wrapper_debugger
