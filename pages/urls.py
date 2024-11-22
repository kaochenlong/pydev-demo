from django.urls import path

from .views import about, contact
from resumes.views import index

app_name = "pages"

urlpatterns = [
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("", index, name="home"),
]
