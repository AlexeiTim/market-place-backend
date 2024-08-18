from django.contrib import admin
from wallet import models
# Register your models here.


@admin.register(models.Wallet)
class WalletAdminModel(admin.ModelAdmin):
    list_display = ('user', 'cash', )