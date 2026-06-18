from pathlib import Path

from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse


class SinglePagesTests(TestCase):
    def test_home_and_about_pages(self):
        expected = {
            reverse("single_pages:home"): "Flask에서 Django로",
            reverse("single_pages:about"): "한 요청이 페이지가 되기까지",
        }
        for route, text in expected.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, text)

    def test_shared_navigation_uses_named_urls(self):
        response = self.client.get(reverse("single_pages:home"))
        self.assertContains(response, 'href="/"')
        self.assertContains(response, 'href="/about/"')
        self.assertContains(response, 'href="/blog/"')

    def test_static_files_are_namespaced_and_safe(self):
        css_path = finders.find("single_pages/css/style.css")
        js_path = finders.find("single_pages/js/main.js")
        bootstrap_path = finders.find("single_pages/css/bootstrap.min.css")
        self.assertTrue(css_path)
        self.assertTrue(js_path)
        self.assertTrue(bootstrap_path)
        javascript = Path(js_path).read_text(encoding="utf-8")
        self.assertIn("textContent", javascript)
        self.assertNotIn("innerHTML", javascript)

    def test_home_loads_static_urls(self):
        response = self.client.get(reverse("single_pages:home"))
        self.assertContains(response, "/static/single_pages/css/bootstrap.min.css")
        self.assertContains(response, "/static/single_pages/css/style.css")
        self.assertContains(response, "/static/single_pages/js/main.js")
