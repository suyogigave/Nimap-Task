from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    users = models.ManyToManyField(User)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
