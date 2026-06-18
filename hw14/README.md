# Assignment 14 - Django Categories and Tags

## 과제 목표

Assignment 13의 미디어 블로그를 확장하여 게시글에 카테고리와 태그를
지정합니다. 한 게시글에는 하나의 카테고리와 여러 개의 태그를 연결할 수
있습니다. 목록과 상세 페이지에서 카테고리와 태그를 보여 주고, 각각을
클릭하면 관련 게시글만 모아 볼 수 있습니다.

## 새 도구

- Django Admin 필터: 카테고리와 태그를 관리하고 게시글에 지정합니다.
- Slug: 사람이 읽기 쉬운 카테고리와 태그 URL을 만듭니다.
- 자동 테스트: 모델 관계, 필터 페이지와 기존 미디어 기능을 함께 검사합니다.

## 새 문법

- `ForeignKey`: 여러 게시글을 하나의 카테고리에 연결하는 다대일 관계입니다.
- `ManyToManyField`: 여러 게시글과 여러 태그를 서로 연결하는 다대다 관계입니다.
- `on_delete=models.SET_NULL`: 카테고리를 삭제해도 게시글은 남기고 미분류로 만듭니다.
- `related_name="posts"`: `category.posts` 또는 `tag.posts`로 관련 글을 찾습니다.
- `SlugField`: `programming`, `django` 같은 URL용 문자열을 저장합니다.
- `get_object_or_404()`: 없는 카테고리나 태그 URL에는 404 응답을 반환합니다.
- `Post.objects.filter(...)`: 선택한 카테고리나 태그의 게시글만 가져옵니다.

## 이전 과제와의 관계

Assignment 12에서 만든 `Post`, `ListView`, `DetailView`와 Assignment 13의
대표 이미지 및 첨부파일 기능을 그대로 유지합니다. 이번 과제는 게시글을
분류하고 여러 키워드로 연결하는 데이터베이스 관계를 추가합니다.

## 프로젝트 구조

```text
hw14/
├── manage.py
├── requirements.txt
├── config/
├── templates/base.html
├── single_pages/
│   └── static/single_pages/css/style.css
└── blog/
    ├── models.py            # Category, Tag, Post 관계
    ├── admin.py             # 세 모델 등록과 필터
    ├── views.py             # 전체/카테고리/태그 페이지
    ├── urls.py              # category/<slug>, tag/<slug>
    ├── tests.py
    ├── migrations/
    └── templates/blog/
        ├── post_list.html
        └── post_detail.html
```

## 주요 URL

- 전체 게시글: `http://127.0.0.1:8000/blog/`
- 카테고리: `http://127.0.0.1:8000/blog/category/<slug>/`
- 미분류: `http://127.0.0.1:8000/blog/category/no-category/`
- 태그: `http://127.0.0.1:8000/blog/tag/<slug>/`
- Admin: `http://127.0.0.1:8000/admin/`

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw14/requirements.txt
python hw14/manage.py migrate
python hw14/manage.py createsuperuser
python hw14/manage.py runserver --noreload
```

Admin에서 먼저 Categories와 Tags를 만든 뒤 Posts에서 게시글에 연결합니다.
Slug에는 공백 대신 하이픈을 사용한 짧은 영문 문자열을 권장합니다.

## 자동 테스트

```bash
python hw14/manage.py check
python hw14/manage.py makemigrations --check --dry-run
python hw14/manage.py test single_pages blog
```

테스트는 다대일/다대다 관계, 카테고리 삭제 시 미분류 처리, Admin 등록,
전체·카테고리·태그·미분류 페이지, 잘못된 URL의 404 응답, 이미지와 첨부파일
기능을 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: LMS Assignment 14와 13주차 강의자료 분석, Category와 Tag 모델,
  다대일·다대다 관계, Admin, 필터 URL과 화면, Migration, 자동 테스트,
  실제 브라우저 검증 및 README 작성
- 사용 프롬프트: "이미지의 Assignment 14 요구사항과 softeng_2026의 기존
  hw13을 바탕으로 카테고리와 태그 기능을 구현해 주세요. 초보자가 이해할 수
  있게 기존 미디어 기능을 유지하고, 독립 분기에서 개발한 뒤 자동 테스트와
  실제 브라우저 검증을 수행하세요. README에 AI 도구, 용도와 프롬프트를
  기록하고, 원격 main과 충돌이 없음을 확인한 후 GitHub main에 빠르게
  동기화하세요."
