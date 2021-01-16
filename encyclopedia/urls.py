from django.urls import path

from . import views

app_name="encyclopedia"

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.page_view, name="page_view"),
    path("search", views.search, name="search")
]
