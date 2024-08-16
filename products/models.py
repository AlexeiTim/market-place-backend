from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Категория товара', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Brand(models.Model):
    name = models.CharField('Брэнд товара', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'




class Product(models.Model):
    name = models.CharField('Название товара', max_length=255)
    description = models.TextField('Описание товара')
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)
    image_url = models.URLField('Ссылка на картинку товара')
    rating = models.IntegerField('Рейтинг товара', validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ], default=1)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='projects', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='projects', null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    comment = models.TextField('Комментарий к отзыву')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата и время создания отзыва', auto_now_add=True)

    def __str__(self):
        return f'Отзыв на {self.product.name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
