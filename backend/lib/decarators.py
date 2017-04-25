# coding: utf-8

from functools import wraps

from django.conf import settings
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import NotAuthenticated


def require_token(func):
    @wraps(func)
    def wrapper(*args):
        request = args[1]
        received_token = get_authorization_header(request).decode()
        token = getattr(settings, 'TOKEN', None)

        if received_token != token:
            raise NotAuthenticated

        return func(*args)
    return wrapper
