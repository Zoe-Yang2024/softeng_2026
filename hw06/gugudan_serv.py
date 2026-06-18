from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gugudan')  
def gugudan():
    dan = request.args.get('dan', type=int)
    error = None
    rows = []

    if dan is None:
        error = '숫자를 입력해 주세요.'
    elif not 2 <= dan <= 9:
        error = '2단부터 9단까지 입력할 수 있습니다.'
    else:
        rows = [
            {'number': number, 'result': dan * number}
            for number in range(1, 10)
        ]

    status_code = 400 if error else 200
    return render_template(
        'gugudan.html', dan=dan, rows=rows, error=error
    ), status_code


if __name__ == '__main__':
    app.run(debug=True)
