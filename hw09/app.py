from pathlib import Path

import pandas as pd
from flask import Flask, render_template


BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "blog_content.csv"

app = Flask(__name__)


def load_posts():
    """Read every blog row from CSV for the template."""
    dataframe = pd.read_csv(CSV_FILE)
    return dataframe.to_dict(orient="records")


@app.route("/")
def index():
    posts = load_posts()
    categories = sorted({post["category"] for post in posts})
    return render_template(
        "index.html",
        title="CSV Blog",
        active_page="home",
        posts=posts,
        categories=categories,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Assignment 09",
        active_page="about",
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
