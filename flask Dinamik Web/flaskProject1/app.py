from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import  SQLAlchemy




app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dinamik.db"

db=SQLAlchemy(app=app)

from models.model import User

with app.app_context():
    db.create_all()


@app.route('/')
def register():
    return render_template("register.html")

@app.route("/registerform",methods=["POST"])
def registerform():
    name=request.form.get("name")
    email=request.form.get("email")
    phoneNumber=request.form.get("phoneNumber")
    password=request.form.get("password")
    user=User(name=name,email=email,phoneNumber=phoneNumber,password=password)
    db.session.add(user)
    db.session.commit()

    if user:
        return redirect(url_for("login"))

    return redirect(url_for("register"))


@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/loginform",methods=["POST"])
def loginform():

    email=request.form.get("email")
    password=request.form.get("password")

    user=User.query.filter_by(email=email).first()
    print(user.email)
    print(user.password)
    print("***********************************")

    if user:
        if user.password==password:
            return redirect(url_for("index"))
        return render_template("login.html")
    return redirect(url_for("register"))



@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
