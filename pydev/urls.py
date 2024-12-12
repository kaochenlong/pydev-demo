from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("resumes/", include("resumes.urls")),
    path("comments/", include("comments.urls")),
    path("users/", include("users.urls")),
] + debug_toolbar_urls()
