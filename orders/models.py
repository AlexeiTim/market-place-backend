from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    PAYMENT_METHODS = [
        ('cash_on_delivery', 'Оплата по месту'),
        ('prepaid', 'Оплата сразу')
    ]

    created_at = models.DateTimeField('Дата и время создания заказа', auto_now_add=True)
    first_name = models.CharField('Имя заказчика', max_length=100, default='Alexei')
    last_name = models.CharField('Фамилия заказчика', max_length=100, default='Timashkov')
    total_price = models.PositiveIntegerField('Общая цена заказа', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(
        'Метод оплаты',
        max_length=20,
        choices=PAYMENT_METHODS,
        default='cash_on_delivery'
    )
    delivery_address = models.CharField('Адрес доставки', max_length=255)

    def __str__(self):
        return f'Заказ от {self.created_at}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
