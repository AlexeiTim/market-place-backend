from django.contrib import admin
from products import models


@admin.register(models.Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ('name', )