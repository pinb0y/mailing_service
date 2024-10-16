from django.core.management import BaseCommand

from mail_sender.services import prepare_mailings


class Command(BaseCommand):
    """Скрипт для поиска и активации новых рассылок"""

    def handle(self, *args, **options):
        prepare_mailings()
