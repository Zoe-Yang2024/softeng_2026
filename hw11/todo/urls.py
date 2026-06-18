from django.urls import path

from . import views


app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("lists/add/", views.list_create, name="list-add"),
    path("lists/<int:list_id>/", views.detail, name="detail"),
    path("lists/<int:list_id>/items/add/", views.item_add, name="item-add"),
    path("lists/<int:list_id>/delete/", views.list_delete, name="list-delete"),
    path("items/<int:item_id>/toggle/", views.item_toggle, name="item-toggle"),
    path("items/<int:item_id>/delete/", views.item_delete, name="item-delete"),
]
