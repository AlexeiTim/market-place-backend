from django.contrib import admin
from blog import models


@admin.register(models.Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at', )
