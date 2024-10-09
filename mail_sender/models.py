from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО клиента")
    email = models.EmailField(verbose_name="Почта", unique=True)
    comment = models.TextField(verbose_name="Комментарий", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["id"]


class Message(models.Model):
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    PERIODIC_TYPES = (
        ("Месяц", "Месяц"),
        ("День", "День"),
        ("Неделя", "Неделя"),
    )

    STATUS_TYPES = (
        ("Создана", "Создана"),
        ("Запущена", "Запущена"),
        ("Закончена", "Закончена"),
        ("Приостановлена", "Приостановлена"),
        ("Отменена", "Отменена"),
    )

    name = models.CharField(max_length=150, verbose_name="Название рассылки")
    client = models.ManyToManyField(
        Client, verbose_name="клиент", related_name="mailings"
    )
    message = models.ForeignKey(
        Message, on_delete=models.SET_NULL, verbose_name="Сообщение", **NULLABLE
    )
    start_mailing = models.DateField(verbose_name="Дата начала рассылки")
    end_mailing = models.DateField(verbose_name="Дата окончания рассылки")
    periodicity = models.CharField(
        default="Неделя",
        max_length=50,
        verbose_name="Периодичность",
        choices=PERIODIC_TYPES,
    )
    status = models.CharField(
        default="Создана",
        max_length=50,
        verbose_name="Статус рассылки",
        choices=STATUS_TYPES,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class MailingTry(models.Model):

    STATUS_TYPES = (
        ("Успешно", "Успешно"),
        ("Провал", "Провал"),
    )

    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка"
    )
    last_try_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время последней попытки", **NULLABLE
    )
    status = models.CharField(
        default="Успешно", max_length=50, verbose_name="Статус", choices=STATUS_TYPES
    )

    def __str__(self):
        return f"{self.pk} - {self.mailing.name} ({self.status})"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
