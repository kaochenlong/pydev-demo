from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    title = models.CharField(max_length=100)
    skill = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} ({self.skill})"
