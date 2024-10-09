from datetime import datetime

from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from mail_sender.models import Mailing

def launch_new_mailings():
    curr_date = datetime.now()

    mailing_new = Mailing.objects.filter(
        status='Создана',
        start_mailing__lte=curr_date,
        end_mailing__gte=curr_date
    )

    if mailing_new.exists():
        for new_mailing in mailing_new:
            new_mailing.status = 'Запущена'
            new_mailing.save()

def stop_finished_mailings():
    curr_date = datetime.now()

    mailings_finished = Mailing.objects.filter(
        status='Запущена',
        end_mailing__lt=curr_date
    )

    if mailings_finished.exists():
        for new_mailing in mailings_finished:
            new_mailing.status = 'Закончена'
            new_mailing.save()

def prepare_mailings():
    launch_new_mailings()
    stop_finished_mailings()

def send_mailing(periodicity):
    mailing_list = Mailing.objects.filter(
        status='Запущена',
        periodicity=periodicity
    )

    if mailing_list.exists():
        for mailing in mailing_list:
            msg = mailing.message
            subscribers = mailing.client.all()
            for subscriber in subscribers:
                send_mail(
                    subject=msg.title,
                    message=msg.body,
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=(subscriber.email,))


