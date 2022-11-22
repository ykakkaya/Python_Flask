from flask import Flask,Blueprint,jsonify

apiCategories=Blueprint("apiCategories",__name__,url_prefix="/api/categories")

@apiCategories.route("/")
def getAllCategories():
    categories=[{"name":"category1"},
    {"name":"category2"},
    {"name":"category3"}]
    return jsonify({"success": True, "data": categories})