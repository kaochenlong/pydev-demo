from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=100)
    skill = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    favorite_users = models.ManyToManyField(
        User,
        related_name="favorited_resumes",
        through="FavoriteResume",
        through_fields=("resume", "user"),
    )

    def __str__(self):
        return f"{self.title} ({self.skill})"


class FavoriteResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
