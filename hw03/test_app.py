"""Smoke tests for every page in the Streamlit application."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).with_name("app.py")
TOOLS = (
    "구구단",
    "홀수/짝수 판별",
    "단위 변환",
    "소수 판별",
    "범위 내 소수 찾기",
    "팩토리얼",
    "짝수의 합",
)


class StreamlitAppTests(unittest.TestCase):
    def test_every_tool_page_opens_without_error(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()
        self.assertEqual(len(app.exception), 0)

        for tool in TOOLS:
            app.sidebar.radio[0].set_value(tool).run()
            self.assertEqual(len(app.exception), 0, tool)

    def test_even_odd_result(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()
        app.sidebar.radio[0].set_value("홀수/짝수 판별").run()
        app.number_input[0].set_value(7)
        app.button[0].click().run()

        self.assertEqual(len(app.exception), 0)
        self.assertIn("홀수입니다", app.success[0].value)

    def test_prime_range_validation(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()
        app.sidebar.radio[0].set_value("범위 내 소수 찾기").run()
        app.number_input[0].set_value(10)
        app.number_input[1].set_value(1)
        app.button[0].click().run()

        self.assertEqual(len(app.exception), 0)
        self.assertIn("시작 값", app.error[0].value)


if __name__ == "__main__":
    unittest.main()
