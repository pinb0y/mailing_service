from django.core.management import BaseCommand

from mail_sender.services import prepare_mailings


class Command(BaseCommand):

    def handle(self, *args, **options):
        prepare_mailings()

