# coding: utf-8

from django.db import models


class Recipient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'


class SMTP(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    host = models.CharField(max_length=254)
    port = models.IntegerField(blank=True, null=True)
    use_ssl = models.BooleanField(default=True)
    ssl_port = models.IntegerField(blank=True, null=True)
    login = models.CharField(max_length=254)
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def usage_port(self):
        if self.ssl_port and self.ssl_port:
            return self.ssl_port

        return self.port

    class Meta:
        verbose_name = 'SMTP'
        verbose_name_plural = 'SMTPs'


class Action(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)
    name = models.CharField(max_length=30, unique=True)
    recipients = models.ManyToManyField(Recipient)
    smtp = models.ForeignKey(
        SMTP, blank=True, null=True, on_delete=models.SET_NULL)
    sender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'
