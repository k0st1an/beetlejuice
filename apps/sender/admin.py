# coding: utf-8

from django.contrib import admin

from apps.sender.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('__str__', 'status', 'sender', 'subject', 'created')
    readonly_fields = (
        'created', 'status', 'sender', 'subject', 'recipient', 'comment'
    )
