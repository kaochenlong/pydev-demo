from django.urls import path

from .views import about, contact, maintain

urlpatterns = [
    path("about/", about),
    path("contact/", contact),
    path("", maintain),
]
