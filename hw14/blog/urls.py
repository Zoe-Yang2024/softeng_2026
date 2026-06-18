from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("category/<str:slug>/", views.category_page, name="category-page"),
    path("tag/<str:slug>/", views.tag_page, name="tag-page"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
]
