from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sum",methods=["POST"])
def sum():
    
    num1=request.form.get("num1")
    num2=request.form.get("num2")
    total=int(num1)+int(num2)
    return render_template("sum.html",total=total,num1=num1,num2=num2)