# coding: utf-8

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from apps.mailer.models import Action
from core.mailer import send_email


class SenderViewSet(ViewSet):
    http_method_names = ('post',)

    @staticmethod
    def post(request):
        req_action = request.data.get('action', None)
        req_body = request.data.get('body', None)

        try:
            action = Action.objects.get(name=req_action)
        except Action.DoesNotExist:
            return Response({'status': False})

        recipients = [recipient.email for recipient in action.recipients.all()]
        send_from = action.sender

        if not req_body:
            return Response({'status': False})

        if recipients and req_body:
            # todo: add support SMTP options
            if send_email(recipients, req_body, send_from):
                return Response({'status': True})

        return Response({'status': False})

    @staticmethod
    def list(request):
        return Response()
