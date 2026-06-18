from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone


def one_week_hence():
    """Return the default due date for a new item."""
    return timezone.now() + timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo:detail", args=[self.pk])


class ToDoItem(models.Model):
    todo_list = models.ForeignKey(
        ToDoList,
        on_delete=models.CASCADE,
        related_name="items",
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["completed", "due_date", "created_at"]

    def __str__(self):
        return self.title
