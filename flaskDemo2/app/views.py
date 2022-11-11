from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("student.html")

@app.route("/info",methods=["POST"])
def studentInfo():
    # name=request.form["name"]
    # mat=request.form["mat"]
    # fen=request.form["fen"]
    contextData={
         "name":request.form["name"],
         "mat":request.form["mat"],
         "fen":request.form["fen"]
    }
    return render_template("info.html",**contextData)