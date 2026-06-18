# Assignment 10 - Django Personal Homepage

## 과제 목표

Assignment 09의 개인 내용과 CSV 블로그를 Django 프로젝트로
마이그레이션했습니다. `single_pages`와 `blog` App을 분리하고 URL, View,
Template, Static의 연결 과정을 연습합니다.

## 새 도구와 문법

- `manage.py`: Django 명령을 실행하는 입구입니다.
- Project `config`: 전체 설정과 최상위 URL을 관리합니다.
- App `single_pages`: Home과 About 페이지를 담당합니다.
- App `blog`: CSV 읽기와 Blog 페이지를 담당합니다.
- `{% url %}`: URL의 `name`으로 안전하게 링크를 만듭니다.
- `{% load static %}`와 `{% static %}`: CSS와 JavaScript 주소를 만듭니다.
- `include()`: Project URL에서 각 App의 URL을 연결합니다.

## 프로젝트 구조

```text
hw10/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
├── single_pages/
│   ├── urls.py
│   ├── views.py
│   ├── templates/single_pages/
│   └── static/single_pages/
├── blog/
│   ├── data/blog_content.csv
│   ├── urls.py
│   ├── views.py
│   └── templates/blog/
├── templates/base.html
└── README.md
```

## Flask와의 관계

| Flask | Django |
|---|---|
| `@app.route()` | `urls.py`와 `views.py` |
| `render_template()` | `render()` |
| `url_for()` | `{% url %}` |
| `static/style.css` | namespaced App static |
| 한 개의 `app.py` | Project와 여러 App |

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw10/requirements.txt
python hw10/manage.py runserver --noreload
```

브라우저에서 `http://127.0.0.1:8000`을 엽니다. `--noreload`는 OneDrive나
한글 경로에서 자동 재시작 프로세스가 종료되는 현상을 피합니다.

## 자동 테스트

```bash
python hw10/manage.py check
python hw10/manage.py test single_pages blog
```

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: Flask와 Django 구조 비교, Project/App 구성, URL namespace,
  Template/Static 마이그레이션, CSV Blog 연결, 테스트와 README 작성
- 사용 프롬프트: "Assignment 09의 개인 내용과 CSV 블로그를 이용해 LMS의
  Assignment 10 Django 홈페이지를 완성해 주세요. config Project와
  single_pages, blog App을 만들고 urls.py, views.py, templates와 namespaced
  static 구조를 사용해 주세요. 두 App이 독립적으로 URL을 관리하고 Blog는
  자신의 CSV를 읽어 일곱 개 글을 출력해야 합니다. requirements.txt,
  README와 Django 자동 테스트를 추가하고 OneDrive에서 안정적으로 실행할
  수 있도록 --noreload 실행 방법을 기록해 주세요."
