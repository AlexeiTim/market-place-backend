from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length=255)
    content = models.TextField('Контент поста')
    created_at = models.DateTimeField('Дата и время создания поста', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время обновления поста', auto_now=True)
    author = models.ForeignKey(User, verbose_name='Аавтор поста', on_delete=models.CASCADE)
    image = models.ImageField('Изображение поста', upload_to='post_images/', blank=True, null=True)

