from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    created_at = models.DateTimeField('Дата и время создания корзины', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Общая корзина'

    class Meta:
        verbose_name = 'Общая корзина'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='Корзина', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар корзины', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Кол-во товара в корзине', default=1)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name ='Товар корзины'
        verbose_name_plural = 'Товары корзины'

