# coding: utf-8

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from apps.mailer.models import Action
from core.mailer import send_email


class SenderViewSet(ViewSet):
    http_method_names = ('post',)

    @staticmethod
    def post(request):
        if request.method == 'POST':
            req_action = request.data.get('action', None)
            body = request.data.get('body', None)
            actions = Action.objects.filter(enable=True)
            emails = []
            smtp = None

            if not req_action or not body:
                return Response({'status': False})

            for action in actions:
                if action.name == req_action:
                    recipients = action.recipients.all()
                    emails = [recipient.email for recipient in recipients]

                if action.smtp:
                    smtp = action.smtp
                    print(smtp)

            print(emails)
            print(body)
            if emails and body:
                # todo: add support SMTP options
                send_email(emails, body)

            return Response({'status': True})

        return Response({'status': False})

    @staticmethod
    def list(request):
        return Response()
