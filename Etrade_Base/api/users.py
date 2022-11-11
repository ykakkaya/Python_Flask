from flask import Flask,Blueprint,jsonify

apiUsers=Blueprint("apiUsers",__name__,url_prefix="/api/users")

@apiUsers.route("/")
def getAllUsers():
    users=[{"name":"user1","pass":123},
    {"name":"user2","pass":123},
    {"name":"user3","pass":123}]
    return jsonify({"success":True,"data":users})