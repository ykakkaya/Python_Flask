from flask import Flask,Blueprint,jsonify

apiProducts=Blueprint("apiProducts",__name__,url_prefix="/api/products")

@apiProducts.route("/")
def getAllAdmins():
    products=[{"name":"product1","price":300},
    {"name":"product1","price":400},
    {"name":"product1","price":500}]
    return jsonify({"success":True,"data":products})