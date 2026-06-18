"""Structural tests for the Assignment 05 static website."""

from html.parser import HTMLParser
from pathlib import Path
import unittest


REPOSITORY = Path(__file__).resolve().parents[2]
SOURCE = REPOSITORY / "hw05"
PUBLISHED = REPOSITORY / "docs"
PAGES = ("index.html", "about_me.html", "blog_list.html")
SITE_FILES = (*PAGES, "assets/style.css", "assets/main.js")


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])


class StaticSiteTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for relative_path in SITE_FILES:
            with self.subTest(path=relative_path):
                self.assertTrue((SOURCE / relative_path).is_file())
                self.assertTrue((PUBLISHED / relative_path).is_file())

    def test_source_and_published_site_match(self) -> None:
        for relative_path in SITE_FILES:
            with self.subTest(path=relative_path):
                self.assertEqual(
                    (SOURCE / relative_path).read_bytes(),
                    (PUBLISHED / relative_path).read_bytes(),
                )

    def test_pages_have_mobile_and_shared_assets(self) -> None:
        for page in PAGES:
            html = (SOURCE / page).read_text(encoding="utf-8")
            with self.subTest(page=page):
                self.assertIn('name="viewport"', html)
                self.assertIn('href="assets/style.css"', html)
                self.assertIn('src="assets/main.js"', html)
                self.assertNotIn("style=", html)

    def test_navigation_targets_exist(self) -> None:
        for page in PAGES:
            parser = LinkParser()
            parser.feed((SOURCE / page).read_text(encoding="utf-8"))
            for link in parser.links:
                if link.startswith(("http://", "https://", "#")):
                    continue
                target = link.split("#", 1)[0]
                with self.subTest(page=page, link=link):
                    self.assertTrue((SOURCE / target).exists())

    def test_user_input_uses_safe_text_content(self) -> None:
        javascript = (SOURCE / "assets/main.js").read_text(encoding="utf-8")
        self.assertIn("textContent", javascript)
        self.assertNotIn("innerHTML", javascript)


if __name__ == "__main__":
    unittest.main()
