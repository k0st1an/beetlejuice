# coding: utf-8

from django.db import models


class History(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    sender = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
    recipient = models.TextField()
    comment = models.TextField(blank=False)

    def __str__(self):
        recipients = self.recipient.split(',')

        if len(recipients) > 1:
            return 'to %s (+%s)' % (recipients[0], len(recipients) - 1)
        else:
            return 'to %s' % self.recipient

    class Meta:
        ordering = ('-created',)
