from django.db import models


# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField('Дата и время создания заказа', auto_now_add=True)
    first_name = models.CharField('Имя заказчика', max_length=100, default='Alexei')
    last_name = models.CharField('Фамилия заказчика', max_length=100, default='Timashkov')
    total_price = models.PositiveIntegerField('Общая цена заказа', default=1)

    def __str__(self):
        return f'Заказ от {self.created_at}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
