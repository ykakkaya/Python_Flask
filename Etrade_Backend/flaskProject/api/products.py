from flask import Flask,Blueprint,jsonify,request
from etrade.models import Product
apiProducts=Blueprint("apiProducts",__name__,url_prefix="/api/products")

@apiProducts.route("/")
def getAllAdmins():
    products=Product.getAllProducts()
    productList=[]
    for product in products:
        productList.append({
            "id":product.id,
            "name":product.name,
            "description":product.description,
            "price":product.price,
            "discountPrice":product.discountPrice,
            "categoryId":product.categoryId
        })
    return jsonify({"success":True,"data":productList})

@apiProducts.route("/<int:id>",methods=["GET","DELETE","PUT"])
def getProduct(id):
    product=Product.getProductById(id)
    if request.method=="GET":
        if product:
            productObj={"id":product.id,
            "name":product.name,
            "description":product.description,
            "price":product.price,
            "discountPrice":product.discountPrice,
            "categoryId":product.categoryId}
            return jsonify({"success":True,"data":productObj})
        else:
            return jsonify({"success": False, "message": "Product bulunamadı"})

    elif request.method=="DELETE":
        Product.deleteProduct(id)
        return jsonify({"success": False, "message": "product silindi"})

    elif request.method=="PUT":
        name= request.form["name"]
        description=request.form["description"]
        price= request.form["price"]
        discountPrice= request.form["discountPrice"]
        categoryId= request.form["categoryId"]

        Product.updateProduct(id=product.id,
                              name=name,
                              description=description,
                              price=price,
                              discountPrice=discountPrice,
                              categoryId=categoryId)
        return jsonify({"success":True,"message":"product başarıyla güncellendi"})

@apiProducts.route("/addproduct",methods=["POST"])
def addProduct():
    name = request.form["name"]
    description = request.form["description"]
    price = request.form["price"]
    discountPrice = request.form["discountPrice"]
    categoryId = request.form["categoryId"]
    Product.addProduct(name=name,
                       description=description,
                       price=price,
                       discountPrice=discountPrice,
                       categoryId=categoryId)
    return jsonify({"success": True, "message": "product başarıyla eklendi"})




