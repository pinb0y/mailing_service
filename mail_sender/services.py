from datetime import datetime

import pytz
from django.conf import settings
from django.core.mail import send_mail

from mail_sender.models import Mailing, Message


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Mailing.objects.filter(start_mailing__lte=current_datetime).filter(
        status__in=['status'])

    for mailing in mailings:
        send_mail(
                subject=Message.title,
                message=Message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.клиенты.all()]
           )