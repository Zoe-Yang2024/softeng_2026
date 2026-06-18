"""Print one multiplication table selected by the user."""


def multiplication_table(dan: int) -> list[str]:
    """Return the multiplication table for ``dan`` from 1 through 9."""
    if not 2 <= dan <= 9:
        raise ValueError("단은 2부터 9 사이여야 합니다.")
    return [f"{dan} x {number} = {dan * number}" for number in range(1, 10)]


def main() -> None:
    try:
        dan = int(input("출력할 단을 입력하세요 (2-9): "))
        print("\n".join(multiplication_table(dan)))
    except ValueError as error:
        print(f"입력 오류: {error}")


if __name__ == "__main__":
    main()
