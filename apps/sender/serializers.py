# coding: utf-8

from rest_framework import serializers


class EmailSenderSerializer(serializers.Serializer):
    subject = serializers.CharField()
    to = serializers.ListField(child=serializers.CharField())
    text = serializers.CharField(required=False, allow_blank=True)
    html = serializers.CharField()
    sender = serializers.CharField(required=False, allow_blank=True)


class BodyField(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()


class DeliveryToInternalSerializer(serializers.Serializer):
    action = serializers.CharField()
    body = BodyField()
