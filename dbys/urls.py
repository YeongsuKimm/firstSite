from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="hello"), #/polls
    path("programs", views.programs, name="programs"),
    # path("hello/", views.hello, name="hello"),
]
