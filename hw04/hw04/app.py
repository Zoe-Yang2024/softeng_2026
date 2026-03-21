from flask import Flask  ,request, render_template

app = Flask(__name__)

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/gugudan')  
def gugudan():
    
    dan= request.args.get('dan', default=5, type=int)  
    resp = "<html>"
    resp += "<body>"
    resp += f"<h1>구구단 {dan}단 </h1>" 
    
    for x in range(1, 10):
        
        resp += f"{dan} * {x} = <font color='blue'>{dan * x}</font><br>" 
        
    resp += "</body>"
    resp += "</html>"
    
    return resp 

@app.route('/bmi')
def bmi():
    h = request.args.get('height', type=float)
    w = request.args.get('weight', type=float)
    if h and w:
       
        bmi_val = round(w / ((h/100)**2), 2)
        
        if bmi_val < 18.5: status = "저체중"
        elif bmi_val < 23: status = "정상"
        elif bmi_val < 25: status = "과체중"
        else: status = "비만"
        
        return f"BMI 지수: <b>{bmi_val}</b> (결과: {status})"
    return "입력값이 올바르지 않습니다."

if __name__ == '__main__':
    app.run(debug=True)
    