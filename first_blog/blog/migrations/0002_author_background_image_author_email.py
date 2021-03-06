# Generated by Django 4.0.3 on 2022-04-16 13:20

import blog.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.functions.user_directory_path_for_background_image_author_files, verbose_name='Задний фон автора'),
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.URLField(default='https://mail.google.com/', verbose_name='Email автора'),
        ),
    ]
