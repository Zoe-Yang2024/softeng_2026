"""Automated tests for the Assignment 04 Flask application."""

from pathlib import Path
import sys
import unittest


HW04_PATH = Path(__file__).resolve().parent.parent
if str(HW04_PATH) not in sys.path:
    sys.path.insert(0, str(HW04_PATH))

from app import app, calculate_bmi, classify_bmi  # noqa: E402


class CalculationTests(unittest.TestCase):
    def test_bmi_calculation(self) -> None:
        self.assertEqual(calculate_bmi(170, 65), 22.49)

    def test_bmi_requires_positive_values(self) -> None:
        with self.assertRaises(ValueError):
            calculate_bmi(-170, 65)
        with self.assertRaises(ValueError):
            calculate_bmi(170, 0)

    def test_bmi_categories(self) -> None:
        self.assertEqual(classify_bmi(18.0), "저체중")
        self.assertEqual(classify_bmi(22.0), "정상")
        self.assertEqual(classify_bmi(24.0), "과체중")
        self.assertEqual(classify_bmi(26.0), "비만")


class RouteTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_page(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Python Web Tools", response.get_data(as_text=True))

    def test_valid_multiplication_table(self) -> None:
        response = self.client.get("/gugudan?dan=7")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("구구단 7단", body)
        self.assertIn(">63<", body)

    def test_invalid_multiplication_table(self) -> None:
        for value in ("", "abc", "1", "10"):
            with self.subTest(value=value):
                response = self.client.get(f"/gugudan?dan={value}")
                self.assertEqual(response.status_code, 400)
                self.assertIn("입력 오류", response.get_data(as_text=True))

    def test_valid_bmi(self) -> None:
        response = self.client.get("/bmi?height=170&weight=65")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("22.49", body)
        self.assertIn("정상", body)

    def test_invalid_bmi(self) -> None:
        invalid_queries = (
            "",
            "height=abc&weight=65",
            "height=0&weight=65",
            "height=-170&weight=-65",
        )
        for query in invalid_queries:
            with self.subTest(query=query):
                response = self.client.get(f"/bmi?{query}")
                self.assertEqual(response.status_code, 400)
                self.assertIn("입력 오류", response.get_data(as_text=True))

        text_error = self.client.get("/bmi?height=abc&weight=65").get_data(as_text=True)
        self.assertIn("숫자로 입력", text_error)


if __name__ == "__main__":
    unittest.main()
