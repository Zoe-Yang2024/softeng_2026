"""Automated tests for the Assignment 06 Flask template application."""

from pathlib import Path
import sys
import unittest


HW06_PATH = Path(__file__).resolve().parent.parent
if str(HW06_PATH) not in sys.path:
    sys.path.insert(0, str(HW06_PATH))

from gugudan_serv import app  # noqa: E402


class Assignment06Tests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_page_uses_input_form(self) -> None:
        response = self.client.get("/")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('action="/gugudan"', body)
        self.assertIn('type="number"', body)

    def test_static_css_is_available(self) -> None:
        response = self.client.get("/static/style.css")
        try:
            self.assertEqual(response.status_code, 200)
            self.assertIn(".card", response.get_data(as_text=True))
        finally:
            response.close()

    def test_valid_multiplication_table(self) -> None:
        response = self.client.get("/gugudan?dan=7")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("구구단 7단", body)
        self.assertIn("7 × 9 = 63", body)

    def test_invalid_multiplication_table(self) -> None:
        for value in ("", "abc", "1", "10"):
            with self.subTest(value=value):
                response = self.client.get(f"/gugudan?dan={value}")
                self.assertEqual(response.status_code, 400)
                self.assertIn("입력을 확인해 주세요", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
