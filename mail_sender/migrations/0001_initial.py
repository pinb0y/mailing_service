# Generated by Django 5.1.1 on 2024-09-14 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="ФИО клиента")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Почта"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Massage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Сообщение")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название рассылки"),
                ),
                (
                    "start_mailing",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время начала рассылки"
                    ),
                ),
                (
                    "end_mailing",
                    models.DateTimeField(
                        verbose_name="Дата и время окончания рассылки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("Месяц", "Месяц"),
                            ("День", "День"),
                            ("Неделя", "Неделя"),
                        ],
                        default="Неделя",
                        max_length=50,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Создана", "Создана"),
                            ("Запущена", "Запущена"),
                            ("Закончена", "Закончена"),
                            ("Приостановлена", "Приостановлена"),
                            ("Отменена", "Отменена"),
                        ],
                        default="Создана",
                        max_length=50,
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(
                        related_name="mailings",
                        to="mail_sender.client",
                        verbose_name="клиент",
                    ),
                ),
                (
                    "massage",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mail_sender.massage",
                        verbose_name="Сообщение",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MailingTry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_try_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время последней попытки"
                    ),
                ),
                ("status", models.BooleanField(verbose_name="статус")),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mail_sender.client",
                        verbose_name="Клиент",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mail_sender.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылок",
            },
        ),
    ]
