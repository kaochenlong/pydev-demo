from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=100)
    skill = models.CharField(max_length=300, null=True)
    content = models.TextField(null=True)
