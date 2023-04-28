from django.urls import path

from . import views

urlpatterns = [
    path("", views.student, name="student"),
    path("", views.postuser, name="postuser"),
    path("", views.index, name="index"),

]
