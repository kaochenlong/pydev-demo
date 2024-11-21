from django.urls import path
from .views import home, new

urlpatterns = [
    path("", home),
    path("new", new),
]
