# Assignment 08 - Bootstrap Personal Homepage

## 과제 목표

Assignment 07의 Flask 개인 홈페이지에 Bootstrap을 적용했습니다. 공통
레이아웃과 반응형 Grid를 사용하고, CSV에 저장한 블로그 글을 Pandas로
읽어 Jinja 반복문으로 출력합니다.

## 새로 사용한 도구와 문법

- Bootstrap: `container`, `row`, `col-*`, `card`, `btn` 등의 클래스로
  반응형 화면을 구성합니다.
- Pandas: `pd.read_csv()`로 `blog_content.csv`를 읽습니다.
- CSV: 블로그의 분류, 날짜, 제목, 본문을 행 단위로 저장합니다.
- Jinja: `{% for %}`로 글과 분류를 반복 출력하고 `{% if %}`로 데이터
  유무와 현재 메뉴를 확인합니다.

## 프로젝트 구조

```text
hw08/
├── app.py
├── blog_content.csv
├── README.md
├── requirements.txt
├── static/
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── style.css
│   └── main.js
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── about_me.html
│   └── blog_list.html
└── tests/
    └── test_app.py
```

`app.py`는 라우팅과 CSV 읽기를 담당합니다. `layout.html`에는 모든
페이지가 공유하는 내비게이션, CSS, JavaScript와 푸터가 있습니다. 각
페이지는 템플릿 상속을 이용해 자신의 내용만 작성합니다.

## 설치 및 실행

저장소 최상위 폴더에서 다음 명령을 실행합니다.

```bash
python -m pip install -r hw08/requirements.txt
python hw08/app.py
```

브라우저에서 `http://127.0.0.1:5000`을 엽니다.

## 자동 테스트

```bash
python -m unittest discover -s hw08/tests -p "test_*.py" -v
```

테스트는 세 페이지, 로컬 Bootstrap과 정적 파일, CSV의 일곱 개 글,
Jinja 렌더링, 기존 개인 내용과 안전한 JavaScript를 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 과제 분석, Bootstrap 반응형 레이아웃 적용, CSV와
  Pandas 데이터 연결, Flask/Jinja 구조 정리, 테스트와 README 작성
- 사용 프롬프트: "Assignment 07의 전체 개인 내용과 안전한 JavaScript
  상호작용을 유지하면서 Assignment 08을 완성해 주세요. 로컬 Bootstrap
  CSS와 반응형 Grid, card, button, navigation을 사용해 주세요. 블로그의
  일곱 개 글은 blog_content.csv에 저장하고 Pandas로 읽은 뒤 Jinja for/if
  문법으로 출력해 주세요. 다운로드 후 바로 실행할 수 있도록
  requirements.txt, README와 자동 테스트를 추가하고 다른 과제는 수정하지
  마세요. 독립 브랜치에서 테스트한 뒤 충돌이 없을 때 main에 빠르게
  동기화해 주세요."
