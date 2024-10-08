from django.contrib import admin

from mail_sender.models import Mailing, Message, Client


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'start_mailing', 'end_mailing', 'periodicity', 'status')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)