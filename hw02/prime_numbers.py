"""List all prime numbers in an inclusive range."""

from is_prime import is_prime


def primes_between(start: int, end: int) -> list[int]:
    """Return all primes between ``start`` and ``end``, inclusive."""
    if start > end:
        raise ValueError("시작 값은 끝 값보다 클 수 없습니다.")
    return [number for number in range(max(2, start), end + 1) if is_prime(number)]


def main() -> None:
    try:
        start = int(input("시작 정수를 입력하세요: "))
        end = int(input("끝 정수를 입력하세요: "))
        primes = primes_between(start, end)
    except ValueError as error:
        print(f"입력 오류: {error}")
        return

    if primes:
        print(f"{start}부터 {end}까지의 소수: {', '.join(map(str, primes))}")
    else:
        print(f"{start}부터 {end}까지 소수가 없습니다.")


if __name__ == "__main__":
    main()
