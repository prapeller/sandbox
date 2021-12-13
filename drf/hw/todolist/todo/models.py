from django.db import models
from django.conf import settings
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Todo(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
