from turtle import title
from django.db import models

class Articles(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50)
    anons = models.CharField(verbose_name="Анонс", max_length=250)
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'




