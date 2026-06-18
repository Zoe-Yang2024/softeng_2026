"""Assignment 04: Flask web app for multiplication tables and BMI."""

from flask import Flask, render_template, request


app = Flask(__name__)


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI from a height in centimetres and a weight in kilograms."""
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("키와 몸무게는 0보다 커야 합니다.")
    return round(weight_kg / ((height_cm / 100) ** 2), 2)


def classify_bmi(bmi_value: float) -> str:
    """Return the category used in the original assignment."""
    if bmi_value < 18.5:
        return "저체중"
    if bmi_value < 23:
        return "정상"
    if bmi_value < 25:
        return "과체중"
    return "비만"


@app.get("/")
def index():
    """Display the main page containing both input forms."""
    return render_template("index.html")


@app.get("/gugudan")
def gugudan():
    """Validate a dan and return its multiplication table as HTML."""
    raw_dan = request.args.get("dan", "").strip()

    try:
        dan = int(raw_dan)
    except ValueError:
        return render_template("_error.html", message="단은 정수로 입력해 주세요."), 400

    if not 2 <= dan <= 9:
        return render_template("_error.html", message="단은 2부터 9 사이여야 합니다."), 400

    rows = [(number, dan * number) for number in range(1, 10)]
    return render_template("_gugudan_result.html", dan=dan, rows=rows)


@app.get("/bmi")
def bmi():
    """Validate height and weight, then return the BMI result as HTML."""
    raw_height = request.args.get("height", "").strip()
    raw_weight = request.args.get("weight", "").strip()

    if not raw_height or not raw_weight:
        return render_template("_error.html", message="키와 몸무게를 모두 입력해 주세요."), 400

    try:
        height = float(raw_height)
        weight = float(raw_weight)
    except ValueError:
        return render_template("_error.html", message="키와 몸무게는 숫자로 입력해 주세요."), 400

    try:
        bmi_value = calculate_bmi(height, weight)
    except ValueError as error:
        return render_template("_error.html", message=str(error)), 400

    status = classify_bmi(bmi_value)
    return render_template(
        "_bmi_result.html",
        bmi_value=bmi_value,
        status=status,
    )


if __name__ == "__main__":
    # debug=True is convenient for local learning because Flask reloads changes.
    app.run(debug=True)
