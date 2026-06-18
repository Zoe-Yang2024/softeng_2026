from flask import Flask, render_template


app = Flask(__name__)

POSTS = [
    {
        'category': 'Development',
        'datetime': '2026-03-22T08:00',
        'date': '2026.03.22 · 08:00',
        'title': 'Assignment 05 완료',
        'content': 'HTML과 CSS로 개인 홈페이지를 만들고 GitHub Pages에 공개했습니다. 앞으로도 배운 내용을 계속 기록하고 개선할 예정입니다.',
        'featured': True,
    },
    {
        'category': 'Development',
        'datetime': '2026-03-22T07:00',
        'date': '2026.03.22 · 07:00',
        'title': '첫 개인 홈페이지 제작 중',
        'content': '여러 HTML 페이지를 링크하고 하나의 CSS 파일로 공통 디자인을 관리하는 방법을 배우고 있습니다.',
        'featured': False,
    },
    {
        'category': 'Development',
        'datetime': '2026-03-22T03:45',
        'date': '2026.03.22 · 03:45',
        'title': 'Assignment 04 완료',
        'content': 'Flask와 AJAX로 구구단과 BMI 계산기를 만들며 서버와 브라우저가 통신하는 흐름을 경험했습니다.',
        'featured': False,
    },
    {
        'category': 'Daily',
        'datetime': '2026-03-21T20:30',
        'date': '2026.03.21 · 20:30',
        'title': '거래 완료',
        'content': '노트북 구매 시 증정된 이어폰을 판매했습니다. 짧은 거래였지만 직접 소통하고 약속을 맞추는 경험이었습니다.',
        'featured': False,
    },
    {
        'category': 'Daily',
        'datetime': '2026-03-21T19:00',
        'date': '2026.03.21 · 19:00',
        'title': '친구와 외식',
        'content': '친구와 함께 마라탕을 먹었습니다. 예전에 먹었던 맛과는 조금 달랐지만 함께한 시간이 즐거웠습니다.',
        'featured': False,
    },
    {
        'category': 'Daily',
        'datetime': '2026-03-21T17:00',
        'date': '2026.03.21 · 17:00',
        'title': 'Gaming',
        'content': '친구들과 컴퓨터 게임을 했습니다. 전부 졌지만 함께 웃을 수 있어서 괜찮은 하루였습니다.',
        'featured': False,
    },
    {
        'category': 'Cooking',
        'datetime': '2026-03-21T14:00',
        'date': '2026.03.21 · 14:00',
        'title': '콜라 닭다리 도전',
        'content': '콜라를 너무 많이 넣어 고기가 퍽퍽해지고 양념도 잘 배지 않았습니다. 다음에는 양을 조절해 다시 도전하려고 합니다.',
        'featured': False,
    },
]

@app.route('/')
def index():
    return render_template(
        'index.html', title='주조양의 홈', description='전북대학교 스마트팜학과 주조양의 개인 홈페이지', active_page='home'
    )

@app.route('/about')
def about():
    return render_template(
        'about_me.html', title='About Me', description='스마트팜을 공부하는 주조양의 이야기와 미래 목표', active_page='about'
    )

@app.route('/blog')
def blog():
    return render_template(
        'blog_list.html', title='Blog', description='주조양의 웹 개발 학습과 일상 기록', active_page='blog', posts=POSTS
    )


if __name__ == '__main__':
    app.run(debug=True)
