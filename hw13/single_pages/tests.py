from pathlib import Path

from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse


class SinglePageTests(TestCase):
    def test_landing_and_about_pages(self):
        expected = {
            reverse("single_pages:landing"): "한 걸음씩 성장합니다",
            reverse("single_pages:about"): "주조양입니다",
        }
        for url, text in expected.items():
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, text)

    def test_shared_navigation_uses_named_routes(self):
        response = self.client.get(reverse("single_pages:landing"))
        self.assertContains(response, 'href="/"')
        self.assertContains(response, 'href="/about/"')
        self.assertContains(response, 'href="/blog/"')

    def test_about_receives_python_skill_list(self):
        response = self.client.get(reverse("single_pages:about"))
        for skill in ("Python", "Flask", "Django", "HTML &amp; CSS"):
            self.assertContains(response, skill)

    def test_responsive_stylesheet_is_discoverable(self):
        css_path = finders.find("single_pages/css/style.css")
        self.assertTrue(css_path)
        stylesheet = Path(css_path).read_text(encoding="utf-8")
        self.assertIn("@media (max-width: 760px)", stylesheet)
