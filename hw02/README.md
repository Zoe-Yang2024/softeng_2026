# Assignment 02 - Python Basic Programming

## 과제 개요

2주차 수업에서 제시된 파이썬 기초 프로그램을 각각 독립된 파일로
구현했습니다. 조건문, 반복문, 함수, 재귀 함수, 리스트 컴프리헨션,
문자열 포맷팅과 예외 처리를 연습하는 것이 목적입니다.

## 프로그램 목록

| File | Description | Main concepts |
|------|-------------|---------------|
| `gugudan.py` | 선택한 단의 구구단 출력 | 반복문, 포맷팅 |
| `even_odd.py` | 정수의 홀수/짝수 판별 | 나머지 연산, 조건문 |
| `unit_converter.py` | 온도와 길이 단위 변환 | 함수, 조건문, 포맷팅 |
| `is_prime.py` | 입력한 수의 소수 여부 판별 | 함수, 반복문, 조기 반환 |
| `prime_numbers.py` | 범위 안의 모든 소수 출력 | 함수, 반복문, 리스트 컴프리헨션 |
| `factorial.py` | 팩토리얼 계산 | 재귀 함수 |
| `sum_even_numbers.py` | 1부터 입력값까지 짝수 합 계산 | 반복문, 리스트 컴프리헨션 |
| `test_hw02.py` | 핵심 함수 자동 테스트 | `unittest` |

## 실행 방법

Python 3가 설치된 터미널에서 `hw02` 폴더로 이동한 뒤 실행합니다.

```bash
python gugudan.py
python even_odd.py
python unit_converter.py
python is_prime.py
python prime_numbers.py
python factorial.py
python sum_even_numbers.py
```

자동 테스트는 다음 명령으로 실행합니다.

```bash
python -m unittest -v test_hw02.py
```

모든 프로그램은 잘못된 입력을 받으면 오류 메시지를 출력하고 정상적으로
종료하도록 예외 처리를 포함합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 과제 요구사항 정리, 프로그램 구조 작성, 예외 처리 보완,
  자동 테스트 및 README 작성
- 사용 프롬프트 요약: "Assignment 02의 파이썬 기초 문제를 완성하고,
  `hw02` 구조와 저장소 README를 수업 요구사항에 맞게 정리해 주세요."
- 모든 결과는 실행 테스트를 통해 검증했습니다.

AI가 작성에 도움을 준 코드를 학습 목적으로 검토하고 각 함수의 동작을
설명할 수 있도록 주석과 간단한 구조를 사용했습니다.
