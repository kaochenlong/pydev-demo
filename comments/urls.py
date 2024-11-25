from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("<int:id>", views.delete, name="delete"),
]
