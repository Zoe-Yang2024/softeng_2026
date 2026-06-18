from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
]
