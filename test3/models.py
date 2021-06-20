from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    name = models.CharField(max_length=240, verbose_name="Название")
    intro = models.TextField(verbose_name="Описание")
    create_date = models.DateTimeField(auto_now=True)
    poster = models.ImageField(verbose_name="Картинка к посту", upload_to='posters/')

    def __str__(self):
        return self.name


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Стать', blank=True, null=True,
                             related_name='comments_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name="Текст комментария")
