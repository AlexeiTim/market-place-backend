# Generated by Django 5.1 on 2024-08-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash_on_delivery', 'Оплата по месту'), ('prepaid', 'Оплата сразу')], default='cash_on_delivery', max_length=20, verbose_name='Метод оплаты'),
        ),
    ]
