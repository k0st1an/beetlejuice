# coding: utf-8

from django.core.mail import send_mail

import smtplib


def send_email(recipients, body, send_from):
    try:
        send_mail(
            body.get('subject'),
            body.get('message'),
            send_from,
            recipients,
            fail_silently=False,
        )
    except smtplib.SMTPDataError:
        return False

    return True
