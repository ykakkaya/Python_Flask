from flask import Flask,Blueprint,jsonify

apiAdmins=Blueprint("apiAdmins",__name__,url_prefix="/api/admins")

@apiAdmins.route("/")
def getAllAdmins():
    admins=[{"name":"admin1","pass":123},
    {"name":"admin2","pass":123},
    {"name":"admin3","pass":123}]
    return jsonify({"success":True,"data":admins})