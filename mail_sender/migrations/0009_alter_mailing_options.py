# Generated by Django 4.2 on 2024-10-12 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mail_sender", "0008_alter_mailingtry_last_try_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "permissions": [("set_mailing_status", "can_change_mailings_status")],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
