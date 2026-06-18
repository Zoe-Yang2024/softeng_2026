"""Streamlit GUI for the Python exercises from Assignment 02."""

from pathlib import Path
import sys

import streamlit as st


# hw02 is a sibling folder. Adding it to Python's search path lets this app
# reuse the tested functions instead of copying the calculation code.
HW02_PATH = Path(__file__).resolve().parent.parent / "hw02"
if str(HW02_PATH) not in sys.path:
    sys.path.insert(0, str(HW02_PATH))

from even_odd import is_even  # noqa: E402
from factorial import factorial  # noqa: E402
from gugudan import multiplication_table  # noqa: E402
from is_prime import is_prime  # noqa: E402
from prime_numbers import primes_between  # noqa: E402
from sum_even_numbers import sum_even_numbers  # noqa: E402
from unit_converter import CONVERSIONS, convert  # noqa: E402


st.set_page_config(
    page_title="Python 기초 도구 모음",
    page_icon="🐍",
    layout="centered",
)


TOOLS = (
    "구구단",
    "홀수/짝수 판별",
    "단위 변환",
    "소수 판별",
    "범위 내 소수 찾기",
    "팩토리얼",
    "짝수의 합",
)


def show_multiplication_table() -> None:
    """Display the multiplication-table tool."""
    st.header("구구단")
    st.write("2단부터 9단 중 하나를 선택하면 표로 출력합니다.")
    dan = st.slider("단 선택", min_value=2, max_value=9, value=2)

    if st.button("구구단 만들기", type="primary"):
        rows = []
        for number, expression in enumerate(multiplication_table(dan), start=1):
            rows.append({"곱하는 수": number, "계산식": expression})
        st.table(rows)


def show_even_odd() -> None:
    """Display the even-or-odd tool."""
    st.header("홀수/짝수 판별")
    st.write("2로 나눈 나머지가 0이면 짝수, 그렇지 않으면 홀수입니다.")
    number = st.number_input("정수 입력", value=0, step=1)

    if st.button("판별하기", type="primary"):
        result = "짝수" if is_even(int(number)) else "홀수"
        st.success(f"{int(number)}은(는) {result}입니다.")


def show_unit_converter() -> None:
    """Display the temperature-and-length conversion tool."""
    st.header("단위 변환")
    st.write("온도 또는 길이의 단위를 선택하여 변환합니다.")
    labels = {
        "섭씨 → 화씨": "1",
        "화씨 → 섭씨": "2",
        "미터 → 센티미터": "3",
        "센티미터 → 미터": "4",
    }
    label = st.selectbox("변환 방법", list(labels))
    value = st.number_input("변환할 값", value=0.0)

    if st.button("변환하기", type="primary"):
        choice = labels[label]
        source, target, _ = CONVERSIONS[choice]
        result = convert(choice, float(value))
        st.success(f"{value:.2f} {source} = {result:.2f} {target}")


def show_prime_check() -> None:
    """Display the single-number prime checker."""
    st.header("소수 판별")
    st.write("소수는 1과 자기 자신으로만 나누어지는 2 이상의 정수입니다.")
    number = st.number_input("확인할 정수", value=2, step=1)

    if st.button("소수 확인", type="primary"):
        if is_prime(int(number)):
            st.success(f"{int(number)}은(는) 소수입니다.")
        else:
            st.warning(f"{int(number)}은(는) 소수가 아닙니다.")


def show_prime_range() -> None:
    """Display the prime-number range finder."""
    st.header("범위 내 소수 찾기")
    st.write("시작 값부터 끝 값까지 포함된 모든 소수를 찾습니다.")
    start = st.number_input("시작 정수", value=1, step=1)
    end = st.number_input("끝 정수", value=100, step=1)

    if st.button("소수 찾기", type="primary"):
        try:
            primes = primes_between(int(start), int(end))
        except ValueError as error:
            st.error(str(error))
        else:
            if primes:
                st.success(f"총 {len(primes)}개의 소수를 찾았습니다.")
                st.write(", ".join(map(str, primes)))
            else:
                st.info("선택한 범위에는 소수가 없습니다.")


def show_factorial() -> None:
    """Display the recursive factorial calculator."""
    st.header("팩토리얼")
    st.write("n!은 1부터 n까지의 모든 정수를 곱한 값입니다.")
    number = st.number_input(
        "0 이상의 정수",
        min_value=0,
        max_value=900,
        value=5,
        step=1,
    )

    if st.button("팩토리얼 계산", type="primary"):
        result = factorial(int(number))
        st.success(f"{int(number)}! = {result}")


def show_even_sum() -> None:
    """Display the even-number sum calculator."""
    st.header("짝수의 합")
    st.write("1부터 입력한 값까지 존재하는 모든 짝수를 더합니다.")
    end = st.number_input("끝 정수", min_value=1, value=100, step=1)

    if st.button("합계 계산", type="primary"):
        result = sum_even_numbers(int(end))
        st.success(f"1부터 {int(end)}까지 짝수의 합은 {result}입니다.")


def main() -> None:
    """Build the application and route to the selected tool."""
    st.title("🐍 Python 기초 도구 모음")
    st.caption("응용소프트웨어개발 - Assignment 03")
    st.sidebar.title("기능 선택")
    selected_tool = st.sidebar.radio("사용할 도구", TOOLS)
    st.sidebar.info("Assignment 02의 계산 함수를 GUI에서 다시 사용합니다.")

    pages = {
        "구구단": show_multiplication_table,
        "홀수/짝수 판별": show_even_odd,
        "단위 변환": show_unit_converter,
        "소수 판별": show_prime_check,
        "범위 내 소수 찾기": show_prime_range,
        "팩토리얼": show_factorial,
        "짝수의 합": show_even_sum,
    }
    pages[selected_tool]()

    st.divider()
    st.caption("주조양 · 202420921 · OpenAI Codex 사용 내역은 README에 기록")


if __name__ == "__main__":
    main()
