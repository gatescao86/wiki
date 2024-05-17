from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("entry/<str:title>", views.entry, name="entry"),
    path("new_page", views.new_page, name="new_page")
]
