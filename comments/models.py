from django.db import models
from resumes.models import Resume


class Comment(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
