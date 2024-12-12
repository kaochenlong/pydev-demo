from django.urls import path

from resumes.views import index

from .views import about, contact

app_name = "pages"

urlpatterns = [
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("", index, name="home"),
]
