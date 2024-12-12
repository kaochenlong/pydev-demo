from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Comment, CommentAdmin)
