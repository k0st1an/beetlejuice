# coding: utf-8

from django.conf import settings

from apps.sender.models import Action


class SendPulse:
    provider_conf = None

    def send_pulse(self, data):
        if data.get('action'):
            action = Action.objects.get(name=data.get('action'))

            # internal
            email = {
                'text': data['body']['message'],
                'html': data['body']['message'],
                'subject': data['body']['subject'],
                'from': {
                    'name': self.provider_conf['from']['name'],
                    'email': self.provider_conf['from']['email']
                },
                'to': [
                    {'email': client.email} for client in action.recipients.all()
                ]
             }
        else:
            # external
            email = {
                'html': data['html'],
                'text': data.get('text', ''),
                'subject': data['subject'],
                'from': {
                    'name': self.provider_conf['from']['name'],
                    'email': self.provider_conf['from']['email']
                },
                'to': [
                    {'email': client} for client in data['to']
                ]
            }

        return email


class Provider(SendPulse):
    def __call__(self, provider, data):
        if not isinstance(provider, str):
            raise TypeError('got \'%s\' instead str' % type(provider))

        if not hasattr(self, provider):
            raise NotImplementedError('provider \'%s\' not support' % provider)

        if not isinstance(data, dict):
            raise TypeError('got \'%s\' instead dict' % type(data))

        func = getattr(self, provider.lower())
        self.provider_conf = getattr(settings, provider.upper())

        return func(data)


providers = Provider()
