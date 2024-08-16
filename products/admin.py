from django.contrib import admin
from products import models


@admin.register(models.Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', )


@admin.register(models.Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Brand)
class BrandAdminModel(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Review)
class ReviewAdminModel(admin.ModelAdmin):
    list_display = ('created_at', )