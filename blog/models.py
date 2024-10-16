from django.db import models

from mail_sender.models import NULLABLE


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=500)
    body = models.TextField(
        "Текст статьи",
    )
    image = models.ImageField("Картинка", upload_to="blog/photo", **NULLABLE)
    is_published = models.BooleanField("Статус публикации", default=True)
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата и время изменения", auto_now=True)
    slug = models.CharField("Слаг", max_length=500, default="#", editable=False)
    view_counter = models.IntegerField("Счетчик просмотров", default=0, editable=False)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ("id",)

    def __str__(self):
        return f"{self.title}"
