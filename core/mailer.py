# coding: utf-8

from django.conf import settings
from django.core.mail import send_mail


def send_email(recipients, body):
    send_mail(
        body.get('subject'),
        body.get('message'),
        settings.EMAIL_FROM,
        recipients,
        fail_silently=False,
    )
