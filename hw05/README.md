# Assignment 05 - Personal Homepage

## 과제 목표

HTML, CSS와 JavaScript를 사용하여 세 페이지로 구성된 개인 홈페이지를
만들고 GitHub Pages에 공개합니다.

- `index.html`: 홈페이지와 안전한 이름 환영 기능
- `about_me.html`: 나의 배경, 전공과 스마트팜 목표
- `blog_list.html`: 웹 개발 학습과 일상 기록

## 새로 사용한 구조

```text
hw05/
├── README.md
├── index.html
├── about_me.html
├── blog_list.html
├── assets/
│   ├── style.css
│   └── main.js
└── tests/
    └── test_site.py
```

세 HTML 페이지는 같은 CSS와 JavaScript를 사용합니다. 따라서 색상이나
메뉴 디자인을 한 파일에서 수정하면 모든 페이지에 적용됩니다.

## 안전한 사용자 입력

기존 코드는 이름을 `innerHTML`로 출력하여 입력값을 HTML 코드처럼
해석할 수 있었습니다. 개선된 코드는 다음과 같이 `textContent`를
사용하여 이름을 일반 문자로만 표시합니다.

```javascript
message.textContent = `Hello, ${name}!`;
```

## 로컬에서 확인하기

저장소 최상위 폴더에서 실행합니다.

```bash
python -m http.server 8000 --directory hw05
```

브라우저에서 `http://127.0.0.1:8000`을 열고, 종료할 때는 터미널에서
`Ctrl+C`를 누릅니다.

## GitHub Pages

교수자 요구사항에 따라 같은 사이트 파일을 저장소 최상위의 `docs/`에도
보관합니다. GitHub Pages의 게시 원본은 `main` 브랜치의 `/docs`입니다.

## 자동 테스트

```bash
python -m unittest discover -s hw05/tests -p "test_*.py" -v
```

테스트는 세 페이지와 링크, 모바일 설정, 공유 CSS/JavaScript, 안전한
입력 처리, 그리고 `hw05`와 `docs`의 일치 여부를 확인합니다.

## AI 사용 기록

- 사용 도구: OpenAI Codex
- 사용 목적: 기존 홈페이지 분석, HTML 의미 구조 개선, 공통 CSS와
  반응형 디자인, 안전한 JavaScript 입력 처리, Pages 구조와 테스트 작성
- 사용 프롬프트 요약: "기존 Assignment 05를 먼저 분석하고, 확인 후
  개인 내용과 기구 풍선 아이디어를 보존하면서 더 안전하고 완성도 높은
  GitHub Pages 홈페이지로 개선해 주세요."
