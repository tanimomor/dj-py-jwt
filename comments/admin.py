from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'task', 'created_at']
    search_fields = ['content', 'user__username', 'task__title']
    list_filter = ['user__username', 'task__title', 'created_at']
