from django.core.management import BaseCommand


from mail_sender.services import send_mailing


class Command(BaseCommand):
    """Скрипт для запуска еженедельных рассылок"""

    def handle(self, *args, **options):
        send_mailing("Месяц")
