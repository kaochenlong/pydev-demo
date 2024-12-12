from django.urls import path

from comments import views as comment_views

from . import views

app_name = "resumes"

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("new", views.new, name="new"),
    path("<int:id>", views.show, name="show"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/comments", comment_views.index, name="comments"),
    path("<int:id>/public", views.public, name="public"),
    path("<int:id>/like", views.toggle_favorite, name="like"),
]
