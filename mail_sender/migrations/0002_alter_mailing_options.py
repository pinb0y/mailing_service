# Generated by Django 5.1.1 on 2024-09-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
