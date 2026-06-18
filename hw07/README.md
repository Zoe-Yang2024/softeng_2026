# Assignment 07 - Flask Personal Homepage

## 과제 목표

Assignment 05에서 만든 세 페이지 개인 홈페이지를 Flask 템플릿으로
변환했습니다. 공통 레이아웃을 한 파일로 관리하고 Flask에서 전달한
블로그 데이터를 Jinja 문법으로 출력합니다.

## 프로젝트 구조

```text
hw07/
├── zzy.py
├── requirements.txt
├── static/
│   └── style.css
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

블로그 글 제목은 `zzy.py`의 리스트에서 템플릿으로 전달합니다.
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

테스트는 세 라우트와 CSS, 공통 레이아웃, `url_for()`로 만든 링크,
Flask에서 전달한 블로그 데이터가 정상적으로 렌더링되는지 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 개인 홈페이지 분석, Flask 템플릿 상속, 공통 링크,
  동적 블로그 목록, 반응형 CSS, 자동 테스트 및 README 작성
- 사용 프롬프트 요약: "기존 Assignment 07의 개인 내용을 유지하면서
  4주차 수업의 Flask/Jinja 템플릿 요구사항에 맞게 개선해 주세요."
