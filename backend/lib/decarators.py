# coding: utf-8

from functools import wraps

from django.conf import settings
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response


def need_token(func):
    @wraps(func)
    def wrapper(*args):
        if not getattr(settings, 'TOKEN', None):
            return Response({}, status=500)

        request = args[1]
        token = get_authorization_header(request).decode()


        return func(*args)
    return wrapper
