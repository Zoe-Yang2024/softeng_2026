"""Determine whether an integer is even or odd."""


def is_even(number: int) -> bool:
    """Return True when ``number`` is even."""
    return number % 2 == 0


def main() -> None:
    try:
        number = int(input("정수를 입력하세요: "))
    except ValueError:
        print("입력 오류: 정수를 입력해야 합니다.")
        return

    result = "짝수" if is_even(number) else "홀수"
    print(f"{number}은(는) {result}입니다.")


if __name__ == "__main__":
    main()
