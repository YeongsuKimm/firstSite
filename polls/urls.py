from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #/polls
    path("hello/", views.hello, name="hello"),
]
