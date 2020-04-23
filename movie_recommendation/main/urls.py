from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("content/", views.content, name="content"),
    path("collaborative/", views.collaborative, name="collaborative")
]