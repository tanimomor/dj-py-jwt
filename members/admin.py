from django.contrib import admin
from .models import ProjectMember

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'role']
    search_fields = ['user__username', 'project__name', 'role']
    list_filter = ['project__name', 'role']
