# Assignment 04 - Flask Web Application

## 과제 소개

수업에서 학습한 Flask 라우팅, GET 요청, HTML 폼과 AJAX를 이용하여
두 가지 기능을 제공하는 웹 애플리케이션을 만들었습니다.

1. 2단부터 9단까지 출력하는 구구단 도구
2. 키와 몸무게를 입력받는 BMI 계산기

## 새로 사용한 구조

- `app.py`: URL 요청을 받고 계산하는 Python 코드
- `templates/`: Flask가 결과를 넣어 브라우저에 보내는 HTML 파일
- `static/style.css`: 색상, 간격과 반응형 화면을 담당하는 CSS
- `static/app.js`: 브라우저 내장 `fetch()`로 AJAX 요청을 보내고 결과
  영역만 수정하는 JavaScript
- `tests/`: 정상 입력과 잘못된 입력을 자동으로 확인하는 테스트

Python, HTML, CSS, JavaScript를 서로 다른 파일로 분리하면 각 파일의
역할이 명확해지고 오류를 찾기 쉬워집니다.

## 설치 및 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw04/requirements.txt
python hw04/app.py
```

터미널에 표시되는 `http://127.0.0.1:5000`을 브라우저에서 엽니다.
서버를 종료할 때는 터미널에서 `Ctrl+C`를 누릅니다.

## 요청 흐름

```text
사용자 입력 → HTML form → AJAX GET 요청 → Flask route
          ← 결과 영역 수정 ← HTML 결과 반환 ← Python 계산
```

예를 들어 7단을 요청하면 브라우저는 `/gugudan?dan=7`로 요청하고,
Flask는 7단 결과가 들어 있는 HTML 조각을 반환합니다.

## 자동 테스트

```bash
python -m unittest discover -s hw04/tests -p "test_*.py" -v
```

테스트는 정상 계산뿐 아니라 빈 입력, 문자 입력, 범위를 벗어난 단,
0과 음수인 키·몸무게도 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 과제 분석, 입력 검증 수정, Flask/HTML/CSS/JavaScript
  구조 정리, 자동 테스트 및 README 작성
- 사용 프롬프트 요약: "기존 Assignment 04를 초보자가 이해할 수 있는
  구조로 설명하고, 확인 후 Flask 웹 애플리케이션을 적절히 개선해 주세요."
- 기존 주제와 AJAX의 동작 방식은 유지하고, 외부 인터넷 없이도 실행되도록
  jQuery CDN 대신 브라우저 내장 `fetch()`를 사용했습니다.
