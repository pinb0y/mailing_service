from django.contrib import admin

from mail_sender.models import Mailing, Message, Client, MailingTry


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "message",
        "start_mailing",
        "end_mailing",
        "periodicity",
        "status",
        "owner",
    )


@admin.register(MailingTry)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("mailing", "status", "last_try_date",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "owner",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "comment",
        "owner",
    )
