from django.urls import path

from . import views


app_name = "plant_care"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/water/", views.simulate_watering, name="simulate-watering"),
    path("diary/", views.diary_list, name="diary-list"),
    path("diary/new/", views.diary_create, name="diary-create"),
    path("about/", views.about, name="about"),
    path("api/v1/readings/", views.device_reading_api, name="device-reading-api"),
]
