from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Скрипт для создания суперпользователя."""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="pinchuk@gmail.com",
            first_name="Sergey",
            last_name="Pinchuk",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("8447")
        user.save()
