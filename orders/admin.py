from django.contrib import admin
from orders import models


@admin.register(models.Order)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ('created_at', )
