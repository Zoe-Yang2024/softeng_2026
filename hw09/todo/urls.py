from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.ListCreate.as_view(), name="list-add"),

    path("item/<int:item_id>/toggle/", views.item_toggle, name="item-toggle"),

    path("item/<int:item_id>/delete/", views.item_delete, name="item-delete"),
    path("<int:list_id>/delete/", views.list_delete, name="list-delete"),

    path("<int:list_id>/", views.detail, name="list"),
]
