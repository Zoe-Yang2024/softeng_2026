from django.contrib import admin
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTests(TestCase):
    def test_string_and_absolute_url(self):
        post = Post.objects.create(title="첫 글", content="내용")
        self.assertEqual(str(post), f"[{post.pk}] 첫 글")
        self.assertEqual(post.get_absolute_url(), f"/blog/{post.pk}/")

    def test_post_is_registered_in_admin(self):
        self.assertIn(Post, admin.site._registry)


class PostViewTests(TestCase):
    def setUp(self):
        self.old_post = Post.objects.create(title="이전 글", content="첫 번째 내용")
        self.new_post = Post.objects.create(
            title="Django CBV 배우기",
            content="ListView와 DetailView를 연결합니다.",
        )

    def test_list_view_uses_cbv_template_and_context(self):
        response = self.client.get(reverse("blog:post-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertEqual(list(response.context["post_list"]), [self.new_post, self.old_post])

    def test_list_page_renders_database_posts(self):
        response = self.client.get(reverse("blog:post-list"))
        self.assertContains(response, "Django CBV 배우기")
        self.assertContains(response, "이전 글")
        self.assertContains(response, self.new_post.get_absolute_url())

    def test_detail_view_renders_selected_post(self):
        response = self.client.get(self.new_post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertEqual(response.context["post"], self.new_post)
        self.assertContains(response, "ListView와 DetailView를 연결합니다")
        self.assertNotContains(response, "첫 번째 내용")

    def test_missing_post_returns_404(self):
        response = self.client.get(reverse("blog:post-detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_empty_list_explains_admin_next_step(self):
        Post.objects.all().delete()
        response = self.client.get(reverse("blog:post-list"))
        self.assertContains(response, "아직 게시글이 없습니다")
        self.assertContains(response, "Admin 페이지")
