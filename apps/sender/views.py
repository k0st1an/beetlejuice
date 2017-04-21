# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.lib.decarators import require_token
from apps.sender.serializers import EmailSenderSerializer


class EmailMessage:
    def __init__(self, subject, to, html, text=None):
        self.to = to
        self.subject = subject
        self.text = text or ''
        self.html = html


class DeliveryToRecipientView(APIView):
    serializer_class = EmailSenderSerializer

    @require_token
    def post(self, request):
        
        return Response({}, status=200)
