# Assignment 09 - Flask CSV Blog

## 과제 목표

CSV 파일에 저장한 블로그 데이터를 Pandas로 읽고 Flask와 Jinja를 이용해
웹페이지에 출력합니다. 데이터, Python 처리, HTML 화면이 서로 분리되는
과정을 연습합니다.

## 새 도구와 문법

- CSV: 블로그 글을 행과 열로 저장합니다.
- Pandas `read_csv()`: CSV를 표 형태로 읽습니다.
- `to_dict(orient="records")`: 각 행을 Jinja가 사용할 수 있는 딕셔너리로
  변환합니다.
- Jinja `{% for %}`와 `{% if %}`: 데이터 수만큼 글을 반복 출력하고,
  데이터가 비어 있는 경우도 처리합니다.

## 프로젝트 구조

```text
hw09/
├── app.py
├── blog_content.csv
├── README.md
├── requirements.txt
├── static/
│   ├── bootstrap.min.css
│   └── style.css
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── about.html
└── tests/
    └── test_app.py
```

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw09/requirements.txt
python hw09/app.py
```

브라우저에서 `http://127.0.0.1:5000`을 엽니다. OneDrive 경로에서 Flask
자동 재시작이 종료되는 문제를 피하기 위해 `use_reloader=False`를
사용했습니다. 종료할 때는 터미널에서 `Ctrl+C`를 누릅니다.

## 자동 테스트

```bash
python -m unittest discover -s hw09/tests -p "test_*.py" -v
```

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 GitHub 코드 분석, 잘못된 과제 번호 정리, CSV와 Pandas
  연결, Flask/Jinja 구조 작성, Bootstrap 화면, 테스트와 README 작성
- 사용 프롬프트: "LMS의 Assignment 09 요구사항에 따라 Flask가
  blog_content.csv를 Pandas로 읽고 Jinja 반복문으로 일곱 개의 글을
  홈페이지에 출력하도록 완성해 주세요. 기존에 hw09에 잘못 올라간 Django
  Todo 코드는 삭제하지 말고 별도 archive에 원본 그대로 보존해 주세요.
  다운로드 후 바로 실행할 수 있도록 requirements.txt, README와 자동
  테스트를 추가하고, OneDrive 경로에서도 Flask 서버가 안정적으로
  실행되도록 자동 reloader를 끄세요."
