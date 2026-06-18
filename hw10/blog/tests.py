from django.test import TestCase
from django.urls import reverse

from .views import load_posts


class BlogTests(TestCase):
    def test_csv_has_seven_posts(self):
        posts = load_posts()
        self.assertEqual(len(posts), 7)
        self.assertTrue(posts[0]["featured"])
        self.assertFalse(posts[1]["featured"])

    def test_blog_page_renders_csv_posts(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Assignment 09 CSV 연결")
        self.assertContains(response, "Django 공부 시작")
        self.assertContains(response, "콜라 닭다리 도전")
        self.assertContains(response, "post-card", count=7)

    def test_blog_page_renders_categories(self):
        response = self.client.get(reverse("blog:post_list"))
        for category in ("Cooking", "Daily", "Development", "Learning"):
            self.assertContains(response, category)
