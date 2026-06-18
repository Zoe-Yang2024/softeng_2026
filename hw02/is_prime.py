"""Check whether an integer is prime."""


def is_prime(number: int) -> bool:
    """Return True if ``number`` is a prime number."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main() -> None:
    try:
        number = int(input("소수인지 확인할 정수를 입력하세요: "))
    except ValueError:
        print("입력 오류: 정수를 입력해야 합니다.")
        return

    result = "소수입니다" if is_prime(number) else "소수가 아닙니다"
    print(f"{number}은(는) {result}.")


if __name__ == "__main__":
    main()
