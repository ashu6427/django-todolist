from django.contrib import admin
from base.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):

    fieldsets = [
        ('User information', {'fields': ['user']}),
        ('Task information', {'fields': ['title', 'description']}),
        ('Status', {'fields': ['completed']})
    ]

    list_display = ['user', 'title', 'description', 'completed']


admin.site.register(Task, TaskAdmin)
