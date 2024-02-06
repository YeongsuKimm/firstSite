from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="hello"), #/polls
    path("users/", views.show_users, name = "show_users"),
    path("programs", views.programs, name="programs"),
    path("courses", views.show_courses, name="courses"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
    # path("hello/", views.hello, name="hello"),
]
