# Assignment 11 - Django Todo List

## 과제 목표

Django의 Model, ORM과 SQLite 데이터베이스를 이용하여 Todo List 앱을
만듭니다. 여러 개의 목록을 만들고, 각 목록에 할 일을 추가하며, 완료 상태
변경과 삭제를 웹페이지에서 처리합니다.

## 새 도구와 문법

- Django ORM: Python 객체로 데이터베이스를 조회하고 수정합니다.
- Model과 Migration: 데이터 구조를 Python 클래스로 정의하고 SQLite에
  반영합니다.
- `ForeignKey`: 하나의 목록과 여러 할 일의 관계를 표현합니다.
- `ModelForm`: Model을 기준으로 입력 폼과 유효성 검사를 만듭니다.
- `get_object_or_404()`: 데이터가 없을 때 안전하게 404 응답을 반환합니다.
- `@require_POST`: 데이터를 변경하는 요청을 POST 방식으로 제한합니다.
- `{% csrf_token %}`: 다른 사이트가 사용자를 속여 요청을 보내는 것을
  방지합니다.

## 프로젝트 구조

```text
hw11/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
└── todo/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    ├── migrations/
    ├── static/todo/style.css
    └── templates/todo/
```

`config`는 프로젝트 전체 설정을 담당하고 `todo` App은 Todo 기능을
담당합니다. `ToDoList` 한 개는 `ForeignKey`로 연결된 여러 `ToDoItem`을
가질 수 있습니다. 목록을 삭제하면 연결된 할 일도 함께 삭제됩니다.

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw11/requirements.txt
python hw11/manage.py migrate
python hw11/manage.py runserver --noreload
```

브라우저에서 `http://127.0.0.1:8000`을 엽니다.

## 자동 테스트

```bash
python hw11/manage.py check
python hw11/manage.py makemigrations --check --dry-run
python hw11/manage.py test todo
```

테스트는 Model 기본값과 관계, 페이지 출력, 목록과 할 일 추가, 입력 검증,
완료 상태 변경, POST 제한, 삭제 시 연관 데이터 제거, 404 처리와 CSS를
확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 Assignment 07~10과 역사적 Todo 코드 분석, Django
  Project/App 구조 작성, Model과 Form 설계, 안전한 POST 처리, 반응형 화면,
  Migration, 자동 테스트, 브라우저 검증 및 README 작성
- 사용 프롬프트: "GitHub의 Assignment 07, 08, 09, 10을 회고한 뒤 LMS의
  Assignment 11 Django Todo List를 시작해 주세요. 기존 과제는 수정하지
  말고 독립된 hw11 프로젝트를 만드세요. 목록 및 할 일 추가, 완료 전환과
  삭제 기능을 구현하고 Model, ForeignKey, Migration, ORM, Admin,
  ModelForm, CSRF와 POST 제한을 사용해 주세요. requirements.txt, README,
  반응형 CSS와 자동 테스트를 포함하고, 실행 후 브라우저에서도 검증해
  주세요. AI 도구, 사용 목적과 프롬프트를 README에 기록해 주세요."
