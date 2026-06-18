"""Convert common temperature and length units."""


CONVERSIONS = {
    "1": ("섭씨", "화씨", lambda value: value * 9 / 5 + 32),
    "2": ("화씨", "섭씨", lambda value: (value - 32) * 5 / 9),
    "3": ("미터", "센티미터", lambda value: value * 100),
    "4": ("센티미터", "미터", lambda value: value / 100),
}


def convert(choice: str, value: float) -> float:
    """Convert ``value`` according to a menu ``choice``."""
    if choice not in CONVERSIONS:
        raise ValueError("메뉴에서 1부터 4 사이의 번호를 선택하세요.")
    return CONVERSIONS[choice][2](value)


def main() -> None:
    print("1. 섭씨 -> 화씨")
    print("2. 화씨 -> 섭씨")
    print("3. 미터 -> 센티미터")
    print("4. 센티미터 -> 미터")

    try:
        choice = input("변환 방법을 선택하세요: ").strip()
        value = float(input("변환할 값을 입력하세요: "))
        source, target, _ = CONVERSIONS[choice]
        result = convert(choice, value)
    except KeyError:
        print("입력 오류: 메뉴에서 1부터 4 사이의 번호를 선택하세요.")
        return
    except ValueError as error:
        print(f"입력 오류: {error}")
        return

    print(f"{value:.2f} {source} = {result:.2f} {target}")


if __name__ == "__main__":
    main()
