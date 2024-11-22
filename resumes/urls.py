from django.urls import path
from . import views

app_name = "resumes"

urlpatterns = [
    path("", views.home, name="list"),
    path("new", views.new, name="new"),
]
