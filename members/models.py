from django.db import models
from users.models import User
from projects.models import Project

class ProjectMember(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ])

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"
