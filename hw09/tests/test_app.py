"""Automated tests for Assignment 09."""

from pathlib import Path
import sys
import unittest


HW09_PATH = Path(__file__).resolve().parent.parent
if str(HW09_PATH) not in sys.path:
    sys.path.insert(0, str(HW09_PATH))

from app import app, load_posts  # noqa: E402


class Assignment09Tests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_pages_are_available(self):
        expected = {"/": "CSV로 관리하는", "/about": "CSV 데이터가 웹페이지"}
        for route, text in expected.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertIn(text, response.get_data(as_text=True))

    def test_csv_has_seven_complete_rows(self):
        posts = load_posts()
        self.assertEqual(len(posts), 7)
        required = {"category", "datetime", "date", "title", "content", "featured"}
        for post in posts:
            self.assertTrue(required.issubset(post))
            self.assertTrue(post["title"])
            self.assertTrue(post["content"])

    def test_csv_rows_render_as_cards(self):
        body = self.client.get("/").get_data(as_text=True)
        self.assertIn("Assignment 09 CSV 연결", body)
        self.assertIn("Pandas로 CSV 읽기", body)
        self.assertIn("콜라 닭다리 도전", body)
        self.assertEqual(body.count("post-card"), 7)

    def test_local_styles_are_available(self):
        expected = {
            "/static/bootstrap.min.css": ".container",
            "/static/style.css": ".post-card",
        }
        for path, marker in expected.items():
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(marker, response.get_data(as_text=True))
                finally:
                    response.close()

    def test_internal_links_use_flask_routes(self):
        body = self.client.get("/").get_data(as_text=True)
        self.assertIn('href="/"', body)
        self.assertIn('href="/about"', body)
        self.assertNotIn("index.html", body)


if __name__ == "__main__":
    unittest.main()
