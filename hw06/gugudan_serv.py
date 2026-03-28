from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/gugudan')  
def gugudan():
    
    dan= request.args.get('dan', default=5, type=int) 
    return render_template('gugudan.html', dan=dan)


if __name__ == '__main__':
    app.run(debug=True)
    