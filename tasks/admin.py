from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']
    search_fields = ['title', 'status', 'priority', 'assigned_to__username', 'project__name']
    list_filter = ['status', 'priority', 'project__name', 'created_at', 'due_date']
