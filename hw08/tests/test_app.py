"""Automated tests for Assignment 08."""

from pathlib import Path
import sys
import unittest


HW08_PATH = Path(__file__).resolve().parent.parent
if str(HW08_PATH) not in sys.path:
    sys.path.insert(0, str(HW08_PATH))

from app import app, load_posts  # noqa: E402


class Assignment08Tests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_required_routes(self):
        expected = {
            "/": "농업의 미래",
            "/about": "농촌에서 시작된 이야기",
            "/blog": "작은 배움과",
        }
        for route, text in expected.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertIn(text, response.get_data(as_text=True))

    def test_pages_use_shared_bootstrap_layout(self):
        for route in ("/", "/about", "/blog"):
            with self.subTest(route=route):
                body = self.client.get(route).get_data(as_text=True)
                self.assertIn('name="viewport"', body)
                self.assertIn('/static/bootstrap.min.css', body)
                self.assertIn('class="navbar', body)
                self.assertIn('href="/about"', body)
                self.assertIn('href="/blog"', body)

    def test_csv_contains_seven_complete_posts(self):
        posts = load_posts()
        self.assertEqual(len(posts), 7)
        required_fields = {
            "category", "datetime", "date", "title", "content", "featured"
        }
        for post in posts:
            self.assertTrue(required_fields.issubset(post))
            self.assertTrue(post["title"])
            self.assertTrue(post["content"])

    def test_csv_posts_are_rendered_by_blog_template(self):
        body = self.client.get("/blog").get_data(as_text=True)
        for title in ("Assignment 05 완료", "친구와 외식", "콜라 닭다리 도전"):
            self.assertIn(title, body)
        self.assertEqual(body.count('class="card border-0 shadow-sm mb-4 post-card'), 7)
        self.assertNotIn("Lorem ipsum", body)

    def test_local_static_files_are_available(self):
        expected = {
            "/static/bootstrap.min.css": ".container",
            "/static/style.css": ".hero-section",
            "/static/main.js": "textContent",
        }
        for path, text in expected.items():
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(text, response.get_data(as_text=True))
                finally:
                    response.close()

    def test_javascript_avoids_unsafe_html_insertion(self):
        response = self.client.get("/static/main.js")
        try:
            body = response.get_data(as_text=True)
            self.assertIn("textContent", body)
            self.assertNotIn("innerHTML", body)
        finally:
            response.close()


if __name__ == "__main__":
    unittest.main()
