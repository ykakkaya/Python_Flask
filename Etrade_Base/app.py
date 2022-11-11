from flask import Blueprint, Flask, jsonify
from api.users import apiUsers
from api.admins import apiAdmins
from api.products import apiProducts

app=Flask(__name__)

app.register_blueprint(apiUsers)
app.register_blueprint(apiAdmins)
app.register_blueprint(apiProducts)

@app.route("/")
def index():
    return jsonify({"success":True,"message":"index page"})


@app.route("/share")
def share():
    shares=["ali","ayse","kaya"]
    return jsonify({"success":True,"data":shares})


if __name__=="__main__":
    app.run(debug=True)