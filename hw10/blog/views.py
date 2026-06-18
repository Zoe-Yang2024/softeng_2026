import csv
from pathlib import Path

from django.shortcuts import render


CSV_FILE = Path(__file__).resolve().parent / "data" / "blog_content.csv"


def load_posts():
    """Read the same CSV content used by Assignment 09."""
    with CSV_FILE.open(encoding="utf-8-sig", newline="") as csv_file:
        posts = list(csv.DictReader(csv_file))

    for post in posts:
        post["featured"] = post["featured"] == "1"
    return posts


def post_list(request):
    posts = load_posts()
    categories = sorted({post["category"] for post in posts})
    return render(
        request,
        "blog/post_list.html",
        {
            "title": "Blog",
            "description": "Django View가 CSV 데이터를 전달하는 블로그",
            "active_page": "blog",
            "posts": posts,
            "categories": categories,
        },
    )
