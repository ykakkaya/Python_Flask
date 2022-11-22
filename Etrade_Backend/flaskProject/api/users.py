from flask import Flask, Blueprint, jsonify, request
from etrade.models import User

apiUsers = Blueprint("apiUsers", __name__, url_prefix="/api/users")


@apiUsers.route("/")
def getAllUsers():
    allUsers = []
    users = User.getAllUsers()
    for user in users:
        allUsers.append({"id": user.id, "username": user.username, "email": user.email, "password": user.password})

    return jsonify({"success": True, "data": allUsers})


@apiUsers.route("/<int:id>", methods=["GET", "DELETE","PUT"])
def getUser(id):
    user = User.getUserById(id)

    if request.method == "GET":
        if user:
            userObj = {"id": user.id, "username": user.username, "email": user.email, "password": user.password}
            return jsonify({"success": True, "data": userObj})
        else:
            return jsonify({"success": False, "message": "User bulunamadı"})

    elif request.method == "DELETE":
        if user:
            User.deleteUser(id=id)
            return jsonify({"success": True, "message": "User başarıyla silindi"})
        else:
            return jsonify({"success": False, "message": "User bulunamadı"})

    elif request.method == "PUT":

        if user:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            User.updateUser(user.id,username=username,email=email,password=password)
            return jsonify({"success": True, "message": "User başarıyla güncellendi"})

        else:
            return jsonify({"success": False, "message": "User bulunamadı"})


@apiUsers.route("/adduser", methods=["GET", "POST"])
def addUser():
    # print("karşılayan method: ", request.method)
    # print("request.data method: ", request.data)
    print("request.form method: ", request.form)
    # print("request.args method: ", request.args)
    try:

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        print(username)
        print(email)
        print(password)

        User.add_User(username=username, email=email, password=password)
        return jsonify({"success": True, "message": "user başarıyla eklendi"})

    except Exception as e:
        print("error measj: ", e)
        return jsonify(({"success": False, "message": "bir hatayla karşılaşılsı"}))
