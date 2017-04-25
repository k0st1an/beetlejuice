# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from backend.lib.sender import Sender
from backend.lib.decarators import require_token
from apps.sender.serializers import (
    DeliveryToExternalSerializer, DeliveryToInternalSerializer
)


class BaseView(APIView):
    serializer_class = None

    def post(self, request):
        email = self.serializer_class(data=request.data)

        if not email.is_valid():
            raise ParseError(email.errors)

        send = Sender(email.validated_data)

        if not send.send():
            Response({'status': False}, status=400)

        return Response({'status': True}, status=200)


class DeliveryToInternalView(BaseView):
    serializer_class = DeliveryToInternalSerializer


class DeliveryToExternalView(BaseView):
    serializer_class = DeliveryToExternalSerializer

    @require_token
    def post(self, request):
        return super(DeliveryToExternalView, self).post(request)
