from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("resumes/", include("resumes.urls")),
    path("comments/", include("comments.urls")),
    path("users/", include("users.urls")),
]
