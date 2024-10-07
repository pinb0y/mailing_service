from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО клиента')
    email = models.EmailField(verbose_name='Почта', unique=True)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['name']


class Massage(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    PERIODIC_TYPES = (
        ('Месяц', 'Месяц'),
        ('День', 'День'),
        ('Неделя', 'Неделя'),
    )

    STATUS_TYPES = (
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена'),
        ('Закончена', 'Закончена'),
        ('Приостановлена', 'Приостановлена'),
        ('Отменена', 'Отменена'),
    )

    name = models.CharField(max_length=150, verbose_name='Название рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиент', related_name='mailings')
    massage = models.ForeignKey(Massage, on_delete=models.SET_NULL, verbose_name='Сообщение', **NULLABLE)
    start_mailing = models.DateTimeField(verbose_name='Дата и время начала рассылки')
    end_mailing = models.DateTimeField(verbose_name='Дата и время окончания рассылки')
    periodicity = models.CharField(default='Неделя', max_length=50, verbose_name='Периодичность',
                                   choices=PERIODIC_TYPES)
    status = models.CharField(default='Создана', max_length=50, verbose_name='Статус рассылки', choices=STATUS_TYPES)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class MailingTry(models.Model):

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.SET_NULL, **NULLABLE)
    last_try_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус')

    def __str__(self):
        return f'{self.pk} - {self.mailing.name} ({self.status})'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
