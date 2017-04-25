# coding: utf-8

from django.contrib import admin

from apps.sender.models import History, Action, Recipient


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('sender', 'subject', 'recipient', 'comment')
    list_display = ('__str__', 'status', 'sender', 'subject', 'created')
    readonly_fields = (
        'created', 'status', 'sender', 'subject', 'recipient', 'comment'
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('name',)
    list_display = ('__str__', 'sender', 'updated', 'created')
    list_filter = ('enable',)
    readonly_fields = ('created', 'updated')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('name', 'email')
    list_display = ('__str__', 'email', 'updated', 'created')
    readonly_fields = ('created', 'updated')
