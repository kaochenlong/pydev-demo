from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from resumes.models import Resume


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-id").filter(deleted_at=None)


class Comment(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)

    objects = CommentManager()

    def __str__(self):
        return self.content

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
