from django.contrib import admin
from cart import models


@admin.register(models.Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ('created_at',)


@admin.register(models.CartItem)
class CartItemAdminModel(admin.ModelAdmin):
    list_display = ('product', 'quantity',)