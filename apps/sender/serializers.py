# coding: utf-8

from rest_framework import serializers


class EmailSenderSerializer(serializers.Serializer):
    subject = serializers.CharField()
    to = serializers.ListField()
    text = serializers.CharField(required=False, allow_blank=True)
    html = serializers.CharField()
