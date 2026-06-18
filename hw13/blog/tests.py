from pathlib import Path
from tempfile import TemporaryDirectory

from django.conf import settings
from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.test import override_settings
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

    def test_posts_without_images_use_the_default_image(self):
        response = self.client.get(reverse("blog:post-list"))
        self.assertContains(response, "single_pages/images/default-post.svg", count=2)


class PostMediaTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.addCleanup(self.media_directory.cleanup)
        self.settings_override = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.settings_override.enable()
        self.addCleanup(self.settings_override.disable)

        self.post = Post.objects.create(
            title="미디어 파일 테스트",
            content="이미지와 첨부파일을 확인합니다.",
            head_image=SimpleUploadedFile(
                "cover.png",
                b"test image content",
                content_type="image/png",
            ),
            file_upload=SimpleUploadedFile(
                "assignment-notes.txt",
                b"download me",
                content_type="text/plain",
            ),
        )

    def test_model_returns_attachment_name_and_extension(self):
        self.assertEqual(self.post.get_file_name(), "assignment-notes.txt")
        self.assertEqual(self.post.get_file_ext(), "txt")

    def test_list_page_displays_uploaded_image(self):
        response = self.client.get(reverse("blog:post-list"))
        self.assertContains(response, self.post.head_image.url)
        self.assertContains(response, "미디어 파일 테스트 대표 이미지")

    def test_detail_page_displays_image_and_download_link(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, self.post.head_image.url)
        self.assertContains(response, self.post.file_upload.url)
        self.assertContains(response, "assignment-notes.txt")
        self.assertContains(response, "첨부파일 다운로드")
        self.assertContains(response, "download")

    def test_media_url_and_generated_file_urls_are_configured(self):
        self.assertEqual(settings.MEDIA_URL, "/media/")
        self.assertTrue(self.post.head_image.url.startswith(settings.MEDIA_URL))
        self.assertTrue(self.post.file_upload.url.startswith(settings.MEDIA_URL))

    def test_uploaded_files_are_stored_inside_media_root(self):
        image_path = Path(self.media_directory.name) / self.post.head_image.name
        file_path = Path(self.media_directory.name) / self.post.file_upload.name
        self.assertTrue(image_path.is_file())
        self.assertTrue(file_path.is_file())
