# Assignment 13 - Django Media File Management

## 과제 목표

Assignment 12의 데이터베이스 블로그를 확장하여 Django Admin에서 게시글의
대표 이미지와 일반 첨부파일을 업로드합니다. 목록과 상세 페이지에는 대표
이미지를 보여 주고, 이미지가 없으면 기본 이미지를 사용합니다. 첨부파일이
있으면 상세 페이지에서 파일명과 확장자를 확인하고 다운로드할 수 있습니다.

## 새 도구

- Pillow: Django `ImageField`가 이미지 파일을 다룰 때 사용하는 라이브러리
- Django Media: 사용자가 업로드한 파일을 정적 CSS와 구분하여 관리하는 기능
- `MEDIA_ROOT`: 업로드된 파일이 실제로 저장되는 폴더
- `MEDIA_URL`: 브라우저에서 업로드 파일에 접근할 때 사용하는 URL 시작 부분

## 새 문법

- `ImageField`: 게시글의 대표 이미지를 저장합니다.
- `FileField`: 이미지가 아닌 일반 첨부파일도 저장합니다.
- `upload_to`: 파일을 `blog/images/연/월/일` 또는 `blog/files/연/월/일`로
  나누어 저장합니다.
- `blank=True`: 이미지와 첨부파일을 선택 항목으로 만듭니다.
- `{{ post.head_image.url }}`: 저장된 이미지의 브라우저 주소를 가져옵니다.
- `{% if post.head_image %}`: 이미지가 있는 경우와 없는 경우를 구분합니다.
- HTML `download`: 링크를 클릭했을 때 첨부파일 다운로드를 요청합니다.

## 이전 과제와의 관계

Assignment 12에서 만든 `Post` Model, Django Admin, `ListView`, `DetailView`를
그대로 사용합니다. 이번 과제는 기존 Post에 `head_image`와 `file_upload`라는
두 개의 선택 필드를 추가합니다. 데이터베이스에는 파일 자체가 아니라 파일의
상대 경로가 저장되고, 실제 파일은 `media/` 폴더에 저장됩니다.

## 프로젝트 구조

```text
hw13/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py          # MEDIA_ROOT와 MEDIA_URL
│   └── urls.py              # 개발 환경의 미디어 URL
├── templates/base.html
├── single_pages/
│   ├── templates/single_pages/
│   └── static/single_pages/
│       ├── css/style.css
│       └── images/default-post.svg
└── blog/
    ├── models.py            # ImageField와 FileField
    ├── admin.py
    ├── tests.py
    ├── migrations/
    └── templates/blog/
        ├── post_list.html
        └── post_detail.html
```

`media/`와 `db.sqlite3`는 실행 중 만들어지는 로컬 데이터이므로 Git에
커밋하지 않습니다.

## 설치와 실행

저장소 최상위 폴더에서 실행합니다.

```bash
python -m pip install -r hw13/requirements.txt
python hw13/manage.py migrate
python hw13/manage.py createsuperuser
python hw13/manage.py runserver --noreload
```

- 홈페이지: `http://127.0.0.1:8000/`
- 게시글 목록: `http://127.0.0.1:8000/blog/`
- Admin: `http://127.0.0.1:8000/admin/`

Admin의 Posts에서 대표 이미지와 첨부파일을 선택해 게시글을 저장한 뒤 Blog
목록과 상세 페이지에서 결과를 확인합니다.

## 자동 테스트

```bash
python hw13/manage.py check
python hw13/manage.py makemigrations --check --dry-run
python hw13/manage.py test single_pages blog
```

테스트는 기존 Landing, About, Admin, ListView와 DetailView 기능에 더해
이미지가 없는 게시글의 기본 이미지, 업로드 이미지 URL, 첨부파일명과 확장자,
다운로드 링크, 미디어 저장 위치와 개발 환경의 미디어 응답을 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 12주차 PDF와 LMS Assignment 13 분석, Django Media 설정,
  `ImageField`와 `FileField`, 이미지가 없을 때의 처리, 첨부파일 다운로드,
  Migration, 반응형 CSS, 자동 테스트, 실제 브라우저 검증과 README 작성
- 사용 프롬프트: "12주차 강의자료와 LMS Assignment 13 요구사항을 이용해
  hw12의 Django Blog를 hw13으로 확장해 주세요. Admin에서 게시글 대표 이미지와
  일반 파일을 업로드하고, 이미지가 없을 때 기본 이미지를 표시하며, 상세
  페이지에서 첨부파일을 다운로드할 수 있게 구현하세요. 기존 과제는 수정하지
  말고 독립 분기에서 작업하세요. README에 AI 도구, 용도와 프롬프트를 기록하고,
  자동 테스트와 실제 브라우저 검증 후 GitHub main에 빠르게 동기화하세요."
