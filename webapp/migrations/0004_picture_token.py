# Generated by Django 5.1 on 2024-08-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_album_is_public_picture_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='token',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True, verbose_name='Токен'),
        ),
    ]
