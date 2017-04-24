# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.lib.sender import External
from backend.lib.decarators import require_token
from apps.sender.serializers import (
    EmailSenderSerializer, DeliveryToInternalSerializer
)


class DeliveryToExternalView(APIView):
    @require_token
    def post(self, request):
        email = EmailSenderSerializer(data=request.data)

        if not email.is_valid():
            return Response(email.errors, status=400)

        send_ext = External(email.validated_data)

        if not send_ext.send():
            Response({'status': False}, status=400)

        return Response({'status': True}, status=200)


class DeliveryToInternalView(APIView):
    @staticmethod
    def post(request):
        email = DeliveryToInternalSerializer(data=request.data)

        if not email.is_valid():
            return Response(email.errors, status=400)

        return Response({'status': True}, status=200)
