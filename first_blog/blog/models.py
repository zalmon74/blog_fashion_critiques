from django.db import models

from .functions import (user_directory_path_for_image_avatar_author_files,
                        user_directory_path_for_background_image_author_files,
                        user_directory_path_for_image_preview_post_files)


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=150)
    image = models.ImageField('Аватар автора', upload_to=user_directory_path_for_image_avatar_author_files)
    background_image = models.ImageField('Задний фон автора',
                                         upload_to=user_directory_path_for_background_image_author_files,
                                         null=True,
                                         blank=True
                                         )
    about_text = models.TextField('Кратко об авторе')
    country = models.CharField('Страна, в которой проживает автор', max_length=100)
    twitter_share = models.URLField('Twitter автора', null=True, blank=True)
    facebook_share = models.URLField('Facebook автора', null=True, blank=True)
    google_plus_share = models.URLField('Google Plus автора', null=True, blank=True)
    email = models.URLField('Email автора', default="https://mail.google.com/")

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        default_related_name = 'author'
        ordering = ('pk',)

    def __str__(self):
        return self.name

    def get_count_posts(self):
        posts_current_author = Post.objects.filter(author=self.pk)
        return posts_current_author.count()

    def get_all_posts_for_current_author(self):
        return Post.objects.filter(author=self.pk)


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    prew = models.TextField('Превью поста')
    image_prew = models.ImageField('Картинка для поста', upload_to=user_directory_path_for_image_preview_post_files,
                                   null=True, blank=True)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE)
    create_post_date = models.DateField("Дата создания поста", auto_now=True)
    last_edit_date = models.DateTimeField("Дата и время последнего изменения поста", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('create_post_date',)

    def get_author_img(self):
        img_author = self.author.image.url
        return img_author

    def get_author_name(self):
        return self.author.name
