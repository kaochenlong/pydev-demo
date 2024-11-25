from django.db import models
from resumes.models import Resume
from django.utils import timezone


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-id").filter(deleted_at=None)


class Comment(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)

    objects = CommentManager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
