from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    summary = models.TextField(max_length=80, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_public = models.BooleanField(default=True, verbose_name='Публичный')

    class Meta:
        db_table = 'album'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'