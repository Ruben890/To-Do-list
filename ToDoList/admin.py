from django.contrib import admin
from .models import Task


@admin.register(Task)
class Admin(admin.ModelAdmin):
    list_display = ('user', 'title', )
