"""Sum all even numbers from 1 through a given upper limit."""


def sum_even_numbers(end: int) -> int:
    """Return the sum of even numbers from 1 through ``end``."""
    if end < 1:
        raise ValueError("끝 값은 1 이상이어야 합니다.")
    even_numbers = [number for number in range(1, end + 1) if number % 2 == 0]
    return sum(even_numbers)


def main() -> None:
    raw_value = input("끝 정수를 입력하세요 (기본값 100): ").strip()
    try:
        end = int(raw_value) if raw_value else 100
        result = sum_even_numbers(end)
    except ValueError as error:
        print(f"입력 오류: {error}")
        return

    print(f"1부터 {end}까지 짝수의 합은 {result}입니다.")


if __name__ == "__main__":
    main()
