# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.lib.sender import Sender
from backend.lib.decarators import require_token
from apps.sender.serializers import (
    EmailSenderSerializer, DeliveryToInternalSerializer
)


class BaseView(APIView):
    serializer_class = None

    def post(self, request):
        email = self.serializer_class(data=request.data)

        if not email.is_valid():
            return Response(email.errors, status=400)

        send_ext = Sender(email.validated_data)

        if not send_ext.send():
            Response({'status': False}, status=400)

        return Response({'status': True}, status=200)


class DeliveryToInternalView(BaseView):
    serializer_class = DeliveryToInternalSerializer


class DeliveryToExternalView(BaseView):
    serializer_class = EmailSenderSerializer

    @require_token
    def post(self, request):
        return super(DeliveryToExternalView, self).post(request)
