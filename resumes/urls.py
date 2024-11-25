from django.urls import path
from . import views
from comments import views as comment_views

app_name = "resumes"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("<int:id>", views.show, name="show"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/comments", comment_views.index, name="comments"),
]
