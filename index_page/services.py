from django.conf import settings
from django.core.cache import cache

from mail_sender.models import Client, Mailing


def get_clients_from_cache():
    """
    Функция возвращает список клиентов из кеша если он включен или из базы данных.
    """

    if not settings.CACHE_ENABLED:
        clients = Client.objects.all()
    else:
        key = "clients"
        clients = cache.get(key)
        if clients is None:
            clients = Client.objects.all()
            cache.set(key, clients)

    return clients


def get_mailings_from_cache():
    """
        Функция возвращает список рассылок из кеша если он включен или из базы данных.
    """

    if not settings.CACHE_ENABLED:
        mailings = Mailing.objects.all()
    else:
        key = "mailings"
        mailings = cache.get(key)
        if mailings is None:
            mailings = Mailing.objects.all()
            cache.set(key, mailings)

    return mailings
