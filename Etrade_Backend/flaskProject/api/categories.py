from flask import Flask, Blueprint, jsonify, request
from etrade.models import Category

apiCategories = Blueprint("apiCategories", __name__, url_prefix="/api/categories")


@apiCategories.route("/")
def getAllCategories():
    allCategories = []
    categories = Category.getAllCategory()
    for category in categories:
        allCategories.append({"id": category.id, "name": category.name})

    return jsonify({"success": True, "data": allCategories})


@apiCategories.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def getById(id):
    category = Category.getCategoryById(id)

    if request.method == "GET":
        if category:
            categoryObj = {"id": category.id, "name": category.name}
            return jsonify({"success": True, "data": categoryObj})
        else:
            return jsonify({"success": False, "message": "Category bulunamadı"})

    elif request.method == "DELETE":
        if category:
            Category.deleteCategory(id)
            return jsonify({"success": True, "message": "Category başarıyla silindi"})
        else:
            return jsonify({"success": False, "message": "Category bulunamadı"})

    elif request.method == "PUT":
        if category:
            name = request.form["name"]
            Category.updateCategory(id=category.id, name=name)
            return jsonify({"success": True, "message": "Category başarıyla güncellendi"})
        else:
            return jsonify({"success": False, "message": "Category bulunamadı"})


@apiCategories.route("/addcategory", methods=["POST"])
def addCategory():
    name = request.form["name"]
    Category.addCategory(name=name)
    return jsonify({"success": True, "message": "Category başarıyla eklendi"})
