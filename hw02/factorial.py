"""Calculate a factorial with a recursive function."""


def factorial(number: int) -> int:
    """Return ``number!`` using recursion."""
    if number < 0:
        raise ValueError("팩토리얼은 0 이상의 정수만 계산할 수 있습니다.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def main() -> None:
    try:
        number = int(input("팩토리얼을 계산할 정수를 입력하세요: "))
        result = factorial(number)
    except ValueError as error:
        print(f"입력 오류: {error}")
        return
    except RecursionError:
        print("입력 오류: 재귀 함수로 계산하기에는 값이 너무 큽니다.")
        return

    print(f"{number}! = {result}")


if __name__ == "__main__":
    main()
