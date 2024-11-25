from django.contrib import admin
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Resume, ResumeAdmin)
