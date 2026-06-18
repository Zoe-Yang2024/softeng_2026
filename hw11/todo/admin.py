from django.contrib import admin

from .models import ToDoItem, ToDoList


class ToDoItemInline(admin.TabularInline):
    model = ToDoItem
    extra = 0


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    search_fields = ["title"]
    inlines = [ToDoItemInline]


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "todo_list", "completed", "due_date"]
    list_filter = ["completed", "todo_list"]
    search_fields = ["title", "description"]
