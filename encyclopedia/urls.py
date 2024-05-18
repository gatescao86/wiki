from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("entry/<str:title>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("error", views.error, name="error"),
    path("<str:title>/edit", views.edit, name="edit"),
    path("random", views.random_page, name="random")
]
