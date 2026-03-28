from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about_me.html')

@app.route('/blog')
def blog():
    return render_template('blog_list.html')


if __name__ == '__main__':
    app.run(debug=True)