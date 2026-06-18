# Assignment 12 - Django Blog List and Detail

## 과제 목표

Django 홈페이지, 자기소개 페이지와 데이터베이스 기반 게시판을 만듭니다.
Admin에서 작성한 게시글을 목록으로 보여 주고, 제목이나 링크를 누르면 해당
게시글의 상세 페이지로 이동하도록 구현합니다.

## 새 도구와 문법

- `Post` Model: 제목, 본문, 작성 시간과 수정 시간을 SQLite에 저장합니다.
- Django Admin: 코드를 수정하지 않고 웹 화면에서 게시글을 작성합니다.
- `ListView`: 여러 Post를 최신 순서로 조회해 목록 템플릿에 전달합니다.
- `DetailView`: URL의 `pk`와 일치하는 Post 한 개를 상세 템플릿에 전달합니다.
- `get_absolute_url()`: 각 게시글의 상세 주소를 Model이 생성합니다.
- `{% load static %}`와 `{% static %}`: App 이름으로 구분된 CSS를 연결합니다.

## FBV와 CBV

`single_pages/views.py`의 Landing과 About은 함수형 뷰(FBV)로 작성했습니다.
요청을 받아 `render()`로 템플릿을 반환하는 흐름을 직접 볼 수 있습니다.

`blog/views.py`의 게시글 목록과 상세 페이지는 클래스형 뷰(CBV)로 작성했습니다.
`ListView`와 `DetailView`가 반복적인 조회와 렌더링 작업을 대신 처리합니다.

## 프로젝트 구조

```text
hw12/
├── manage.py
├── requirements.txt
├── config/
├── templates/base.html
├── single_pages/
│   ├── urls.py
│   ├── views.py
│   ├── templates/single_pages/
│   └── static/single_pages/css/style.css
└── blog/
    ├── admin.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    ├── migrations/
    └── templates/blog/
```

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw12/requirements.txt
python hw12/manage.py migrate
python hw12/manage.py createsuperuser
python hw12/manage.py runserver --noreload
```

- 홈페이지: `http://127.0.0.1:8000/`
- 게시글 목록: `http://127.0.0.1:8000/blog/`
- Admin: `http://127.0.0.1:8000/admin/`

Admin에 로그인하여 Posts에서 게시글을 작성한 뒤 Blog 페이지에서 목록과 상세
페이지를 확인합니다.

## 자동 테스트

```bash
python hw12/manage.py check
python hw12/manage.py makemigrations --check --dry-run
python hw12/manage.py test single_pages blog
```

테스트는 홈페이지, 자기소개, 정적 CSS, Model, Admin 등록, 최신 글 정렬,
ListView, DetailView, 상세 링크, 빈 목록과 404 처리를 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 11주차 PDF와 LMS Assignment 12 분석, FBV와 CBV 비교,
  Django Project/App 구조, Post Model과 Admin, 목록 및 상세 페이지,
  반응형 CSS, Migration, 자동 테스트, 브라우저 검증과 README 작성
- 사용 프롬프트: "제11주 강의의 URL, FBV, CBV, ListView, DetailView,
  static 파일과 LMS Assignment 12 요구사항을 이용해 hw12를 만들어 주세요.
  새 Django 프로젝트에 Landing Page와 자기소개, Admin에서 작성하는 Post
  Model, 최신 게시글 목록과 pk 기반 상세 페이지를 구현하세요. 기존 과제는
  수정하지 말고 독립 분기에서 작업하며 README에 AI 도구, 목적과 프롬프트를
  기록하세요. 자동 테스트와 브라우저 검증 후 GitHub main에 빠르게
  동기화하세요."
