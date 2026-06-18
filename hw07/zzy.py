from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about_me.html', title='About Me')

@app.route('/blog')
def blog():
    posts = [
        '스마트팜에 관심을 가지게 된 이유',
        '응용소프트웨어개발 수업에서 배우고 싶은 것',
        '처음 만들어 본 개인 홈페이지',
    ]
    return render_template('blog_list.html', title='Blog', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
