from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/', verbose_name="Фотография")
    summary = models.CharField(max_length=40, verbose_name='Подпись')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом')

    class Meta:
        db_table = 'picture'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
