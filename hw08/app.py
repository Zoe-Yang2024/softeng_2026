from pathlib import Path

import pandas as pd
from flask import Flask, render_template


BASE_DIR = Path(__file__).resolve().parent
BLOG_DATA_FILE = BASE_DIR / "blog_content.csv"

app = Flask(__name__)


def load_posts():
    """Read blog posts from CSV and return template-friendly dictionaries."""
    dataframe = pd.read_csv(BLOG_DATA_FILE)
    return dataframe.to_dict(orient="records")


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="주조양의 홈",
        description="전북대학교 스마트팜학과 주조양의 개인 홈페이지",
        active_page="home",
    )


@app.route("/about")
def about():
    return render_template(
        "about_me.html",
        title="About Me",
        description="스마트팜을 공부하는 주조양의 이야기와 미래 목표",
        active_page="about",
    )


@app.route("/blog")
def blog():
    posts = load_posts()
    categories = sorted({post["category"] for post in posts})
    return render_template(
        "blog_list.html",
        title="Blog",
        description="주조양의 웹 개발 학습과 일상 기록",
        active_page="blog",
        posts=posts,
        categories=categories,
    )


if __name__ == "__main__":
    app.run(debug=True)
