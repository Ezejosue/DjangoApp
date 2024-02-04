from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Task Model Admin
admin.site.register(Task, TaskAdmin)
