from flask import Flask, Blueprint, jsonify, request
from etrade.models import Admin

apiAdmins = Blueprint("apiAdmins", __name__, url_prefix="/api/admins")


@apiAdmins.route("/")
def getAllAdmins():
    allAdmins = []

    admins = Admin.getAllAdmins()

    for admin in admins:
        allAdmins.append({"id": admin.id, "username": admin.username, "password": admin.password, "email": admin.email,
                          "mod": admin.mod})
    return jsonify({"success": True, "data": allAdmins})


@apiAdmins.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def getAdmin(id):
    admin = Admin.getAdminById(id=id)

    if request.method == "GET":
        if admin:
            userObj = {"id": admin.id, "username": admin.username, "email": admin.email, "password": admin.password,
                       "mod": admin.mod}
            return jsonify({"success": True, "data": userObj})
        else:
            return jsonify({"success": False, "message": "Admin bulunamadı"})

    elif request.method == "DELETE":
        if admin:
            Admin.deleteAdmin(id=id)
            return jsonify({"success": True, "message": "Admin başarıyla silindi"})
        else:
            return jsonify({"success": False, "message": "Admin bulunamadı"})

    elif request.method == "PUT":

        if admin:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            mod = request.form["mod"]
            Admin.updateAdmin(admin.id, username=username, email=email, password=password, mod=mod)
            return jsonify({"success": True, "message": "Admin başarıyla güncellendi"})

        else:
            return jsonify({"success": False, "message": "Admin bulunamadı"})

@apiAdmins.route("/addadmin", methods=["POST"])
def addAdmin():
    username=request.form["username"]
    password=request.form["password"]
    email=request.form["email"]
    mod=request.form["mod"]

    Admin.addAdmin(username=username,email=email,password=password,mod=mod)
    return jsonify({"success": True, "message": "admin başarıyla eklendi"})

