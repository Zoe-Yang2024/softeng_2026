# Assignment 06 - Flask Template Application

## 과제 목표

수업에서 작성한 구구단 웹 서비스를 Flask의 템플릿 기능을 사용하도록
변환했습니다. Python은 요청과 입력 검사를 담당하고, HTML은 화면을,
CSS는 디자인을 담당합니다.

## 프로젝트 구조

```text
hw06/
├── gugudan_serv.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── gugudan.html
└── tests/
    └── test_app.py
```

- `layout.html`: 두 페이지가 공유하는 HTML 구조
- `index.html`: 구구단 입력 폼
- `gugudan.html`: Jinja의 `if`와 `for`를 이용한 결과 화면
- `static/style.css`: 공통 디자인과 반응형 너비

템플릿에서는 하드 코딩한 주소 대신 `url_for()`를 사용했습니다.
입력값은 2부터 9까지만 허용하며, 비어 있거나 문자인 경우에도 사용자가
이해할 수 있는 오류 메시지를 보여줍니다.

## 설치 및 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw06/requirements.txt
python hw06/gugudan_serv.py
```

브라우저에서 `http://127.0.0.1:5000`을 열고, 종료할 때는 터미널에서
`Ctrl+C`를 누릅니다.

## 자동 테스트

```bash
python -m unittest discover -s hw06/tests -p "test_*.py" -v
```

테스트는 홈페이지와 CSS 로딩, 정상적인 구구단 계산, 빈 입력, 문자 입력,
허용 범위를 벗어난 입력을 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 과제 분석, Flask 템플릿 구조 정리, 입력 검증,
  반응형 CSS, 자동 테스트 및 README 작성
- 사용 프롬프트 요약: "기존 Assignment 06의 구구단 기능을 유지하면서
  4주차 수업의 템플릿, static, url_for, Jinja 문법에 맞게 개선해 주세요."
