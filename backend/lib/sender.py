# coding: utf-8

from django.conf import settings

from sendpulse_api import Client

from apps.sender.models import History
from backend.lib.email_providers import providers


# todo: обобщить

class Sender:
    email = None

    def __init__(self, email, provider='send_pulse'):
        self.email = providers(provider, email)
        self.provider_conf = getattr(settings, provider.upper())
        self.send_pulse_key = self.provider_conf['id']
        self.send_pulse_secret = self.provider_conf['secret']
        self.recipients_str = self.recipients_to_str()
        self.subject = self.email['subject']
        self.sender = self.provider_conf['from']['email']

    def send(self):
        if self.sender is None:
            raise NotImplementedError('self.sender is not defined')

        if self.subject is None:
            raise NotImplementedError('self.subject is not defined')

        if self.recipients_str is None:
            raise NotImplementedError('self.recipients_str is not defined')

        if not isinstance(self.email, dict):
            raise TypeError('self.email  is not defined')

        history = History.objects.create(
            sender=self.sender,
            subject=self.subject,
            recipient=self.recipients_str
        )

        client = Client(key=self.send_pulse_key, secret=self.send_pulse_secret)

        res = client.smtp_send_email(self.email)

        if res.get('error_code'):
            history.comment = res['message']
        else:
            history.status = True

        history.save()

        return history.status

    def recipients_to_str(self):
        return ', '.join([recipient['email'] for recipient in self.email['to']])
