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
            "/": "환영합니다",
            "/about": "자기소개",
            "/blog": "최근 글",
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
            "스마트팜에 관심을 가지게 된 이유",
            "응용소프트웨어개발 수업에서 배우고 싶은 것",
            "처음 만들어 본 개인 홈페이지",
        )
        for post in posts:
            self.assertIn(post, body)

    def test_static_css_is_available(self) -> None:
        response = self.client.get("/static/style.css")
        try:
            self.assertEqual(response.status_code, 200)
            self.assertIn("@media", response.get_data(as_text=True))
        finally:
            response.close()


if __name__ == "__main__":
    unittest.main()
