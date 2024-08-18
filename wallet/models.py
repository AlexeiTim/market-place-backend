from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    cash = models.PositiveIntegerField('Кеш кошелька', default=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.cash}'

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'