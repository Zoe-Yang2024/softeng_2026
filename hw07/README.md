# Assignment 07 - Flask Personal Homepage

## 과제 목표

Assignment 05에서 만든 세 페이지 개인 홈페이지의 내용, 반응형 디자인과
안전한 JavaScript 상호작용을 유지하면서 Flask 템플릿으로 변환했습니다.
공통 레이아웃을 한 파일로 관리하고 Flask에서 전달한 블로그 데이터를
Jinja 문법으로 출력합니다.

## 프로젝트 구조

```text
hw07/
├── zzy.py
├── requirements.txt
├── static/
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

`layout.html`에 `<head>`, 제목, 내비게이션과 푸터를 모았습니다. 각 페이지는
`{% extends 'layout.html' %}`와 `{% block content %}`를 사용하므로 중복
코드가 줄어듭니다. 모든 페이지와 정적 파일 링크는 `url_for()`로 만듭니다.

블로그 글의 분류, 날짜, 제목, 내용은 `zzy.py`의 딕셔너리 리스트에서
템플릿으로 전달합니다.
`blog_list.html`은 Jinja의 `if`와 `for`를 사용하여 데이터 유무에 따라
화면을 다르게 표시합니다.

## 설치 및 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw07/requirements.txt
python hw07/zzy.py
```

브라우저에서 `http://127.0.0.1:5000`을 열고 Home, About Me, Blog 메뉴를
확인합니다.

## 자동 테스트

```bash
python -m unittest discover -s hw07/tests -p "test_*.py" -v
```

테스트는 세 라우트와 정적 파일, 공통 레이아웃, `url_for()`로 만든 링크,
일곱 개의 블로그 글, 기존 개인 내용과 안전한 JavaScript가 정상적으로
유지되는지 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 개인 홈페이지 분석, Flask 템플릿 상속, 공통 링크,
  동적 블로그 목록, 반응형 CSS, 자동 테스트 및 README 작성
- 사용 프롬프트: "Assignment 05의 세 페이지 개인 홈페이지를 Assignment
  07 Flask 웹사이트로 변환해 주세요. 기존의 전체 개인 내용, 반응형 CSS와
  textContent를 사용하는 안전한 JavaScript 상호작용을 유지해 주세요.
  layout.html 상속, render_template, url_for, Jinja for/if를 사용하고 일곱
  개 블로그 글은 Python 딕셔너리 리스트에서 템플릿으로 전달해 주세요.
  README, requirements.txt와 자동 테스트도 작성하고 다른 과제는 수정하지
  마세요."
