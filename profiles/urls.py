from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="name"),
    path("get_profiles/", views.get_profiles, name="get_profiles"),
]