# coding: utf-8
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.lib.decarators import require_token


class DeliveryToRecipientView(APIView):
    @require_token
    def post(self, request):
        return Response({})
