from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path("", views.index),
    path("postuser/", views.postuser),
    path("student/", views.student),
    path("admin/", admin.site.urls),
]
