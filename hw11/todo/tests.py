from datetime import timedelta
from pathlib import Path

from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import ToDoItem, ToDoList


class TodoModelTests(TestCase):
    def test_model_defaults_and_relationship(self):
        todo_list = ToDoList.objects.create(title="공부")
        before = timezone.now() + timedelta(days=6, hours=23)
        item = ToDoItem.objects.create(todo_list=todo_list, title="Django 복습")
        after = timezone.now() + timedelta(days=7, minutes=1)

        self.assertEqual(str(todo_list), "공부")
        self.assertEqual(str(item), "Django 복습")
        self.assertFalse(item.completed)
        self.assertLess(before, item.due_date)
        self.assertLess(item.due_date, after)
        self.assertEqual(todo_list.items.get(), item)


class TodoViewTests(TestCase):
    def setUp(self):
        self.todo_list = ToDoList.objects.create(title="이번 주")
        self.item = ToDoItem.objects.create(
            todo_list=self.todo_list,
            title="과제 제출",
            description="동영상도 확인하기",
        )

    def test_index_and_detail_render_data(self):
        index = self.client.get(reverse("todo:index"))
        detail = self.client.get(reverse("todo:detail", args=[self.todo_list.pk]))

        self.assertContains(index, "이번 주")
        self.assertContains(index, "전체 1개")
        self.assertContains(detail, "과제 제출")
        self.assertContains(detail, "동영상도 확인하기")

    def test_empty_index_explains_next_action(self):
        ToDoList.objects.all().delete()
        response = self.client.get(reverse("todo:index"))
        self.assertContains(response, "아직 목록이 없습니다")

    def test_create_list_redirects_to_detail(self):
        response = self.client.post(reverse("todo:list-add"), {"title": "장보기"})
        created = ToDoList.objects.get(title="장보기")
        self.assertRedirects(response, created.get_absolute_url())

    def test_duplicate_list_name_shows_validation_error(self):
        response = self.client.post(reverse("todo:list-add"), {"title": "이번 주"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "이미 존재합니다")
        self.assertEqual(ToDoList.objects.filter(title="이번 주").count(), 1)

    def test_add_item(self):
        response = self.client.post(
            reverse("todo:item-add", args=[self.todo_list.pk]),
            {"title": "테스트 작성", "description": "기능 확인"},
        )
        self.assertRedirects(response, self.todo_list.get_absolute_url())
        self.assertTrue(self.todo_list.items.filter(title="테스트 작성").exists())

    def test_empty_item_is_rejected(self):
        response = self.client.post(
            reverse("todo:item-add", args=[self.todo_list.pk]), {"title": ""}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.todo_list.items.count(), 1)

    def test_toggle_requires_post_and_changes_state(self):
        url = reverse("todo:item-toggle", args=[self.item.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.client.post(url)
        self.item.refresh_from_db()
        self.assertTrue(self.item.completed)

    def test_delete_item_requires_post(self):
        url = reverse("todo:item-delete", args=[self.item.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.client.post(url)
        self.assertFalse(ToDoItem.objects.filter(pk=self.item.pk).exists())

    def test_delete_list_cascades_to_items(self):
        response = self.client.post(
            reverse("todo:list-delete", args=[self.todo_list.pk])
        )
        self.assertRedirects(response, reverse("todo:index"))
        self.assertFalse(ToDoList.objects.filter(pk=self.todo_list.pk).exists())
        self.assertFalse(ToDoItem.objects.filter(pk=self.item.pk).exists())

    def test_missing_objects_return_404(self):
        self.assertEqual(
            self.client.get(reverse("todo:detail", args=[9999])).status_code, 404
        )
        self.assertEqual(
            self.client.post(reverse("todo:item-toggle", args=[9999])).status_code,
            404,
        )

    def test_css_is_available(self):
        css_path = finders.find("todo/style.css")
        self.assertTrue(css_path)
        stylesheet = Path(css_path).read_text(encoding="utf-8")
        self.assertIn(".card-grid", stylesheet)
