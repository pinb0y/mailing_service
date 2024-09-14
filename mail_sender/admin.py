from django.contrib import admin

from mail_sender.models import Mailing, Massage, Client


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'massage', 'start_mailing', 'end_mailing', 'periodicity', 'status')

@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)