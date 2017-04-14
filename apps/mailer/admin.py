# coding: utf-8

from django.contrib import admin

from apps.mailer.models import Action, Recipient, SMTP


class ActionAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('name',)
    list_display = ('name', 'smtp', 'sender')
    list_filter = ('enable',)
    readonly_fields = ('created', 'last_update')


class RecipientAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('name', 'email')
    list_display = ('name', 'email')
    readonly_fields = ('created', 'last_update')


class SMTPAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    search_fields = ('name', 'host')
    list_display = ('name', 'host', 'use_ssl', 'usage_port')
    readonly_fields = ('created', 'last_update')


admin.site.register(SMTP, SMTPAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Recipient, RecipientAdmin)
