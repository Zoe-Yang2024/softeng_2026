"""Automated tests for the Assignment 07 Flask personal homepage."""

from pathlib import Path
import sys
import unittest


HW07_PATH = Path(__file__).resolve().parent.parent
if str(HW07_PATH) not in sys.path:
    sys.path.insert(0, str(HW07_PATH))

from zzy import app  # noqa: E402


class Assignment07Tests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_required_routes(self) -> None:
        expected_text = {
            "/": "농업의 미래",
            "/about": "농촌에서 시작된 이야기",
            "/blog": "작은 배움과",
        }
        for route, text in expected_text.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertIn(text, response.get_data(as_text=True))

    def test_pages_share_layout_and_navigation(self) -> None:
        for route in ("/", "/about", "/blog"):
            with self.subTest(route=route):
                body = self.client.get(route).get_data(as_text=True)
                self.assertIn('name="viewport"', body)
                self.assertIn('href="/"', body)
                self.assertIn('href="/about"', body)
                self.assertIn('href="/blog"', body)
                self.assertIn('href="/static/style.css"', body)

    def test_blog_data_is_rendered(self) -> None:
        body = self.client.get("/blog").get_data(as_text=True)
        posts = (
            "Assignment 05 완료",
            "친구와 외식",
            "콜라 닭다리 도전",
        )
        for post in posts:
            self.assertIn(post, body)
        self.assertEqual(body.count('class="post-card'), 7)

    def test_hw05_personal_content_is_preserved(self) -> None:
        home = self.client.get("/").get_data(as_text=True)
        about = self.client.get("/about").get_data(as_text=True)
        self.assertIn("농업의 미래", home)
        self.assertIn('id="welcome-form"', home)
        self.assertIn("농촌에서 시작된 이야기", about)
        self.assertIn("기술과 지능이 결합된 농장", about)

    def test_safe_javascript_is_available(self) -> None:
        response = self.client.get("/static/main.js")
        try:
            body = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("textContent", body)
            self.assertNotIn("innerHTML", body)
        finally:
            response.close()

    def test_static_css_is_available(self) -> None:
        response = self.client.get("/static/style.css")
        try:
            self.assertEqual(response.status_code, 200)
            self.assertIn("@media", response.get_data(as_text=True))
        finally:
            response.close()


if __name__ == "__main__":
    unittest.main()
