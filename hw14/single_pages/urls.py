from django.urls import path

from . import views


app_name = "single_pages"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("about/", views.about, name="about"),
]
