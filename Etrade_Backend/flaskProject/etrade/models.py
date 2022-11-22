from dataclasses import dataclass
from etrade import db


@dataclass
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password


    @classmethod
    def getAllUsers(cls):
        return cls.query.all()

    @classmethod
    def getUserById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_User(cls, username, email, password):
        user = cls(id=None,username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()

    @classmethod
    def updateUser(cls, id, username, email, password):
        user = cls.query.filter_by(id=id).first()
        user.username = username
        user.email = email
        user.password = password

        db.session.commit()

    @classmethod
    def deleteUser(cls, id):
        user = cls.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()


@dataclass
class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    mod = db.Column(db.Integer, default=True)

    def __init__(self, id, username, email, password, mod):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.mod = mod

    @classmethod
    def getAllAdmins(cls):
        return cls.query.all()

    @classmethod
    def getAdminsById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def addAdmins(cls, username, email, password, mod):
        admin = cls(username=username, email=email, password=password, mod=mod)
        db.session.add(admin)
        db.session.commit()

    @classmethod
    def updateAdmins(cls, id, username, email, password, mod):
        admin = cls.query.filter_by(id=id).first()
        admin.username = username
        admin.email = email
        admin.password = password
        admin.mod = mod
        db.session.commit()

    @classmethod
    def deleteAdmin(cls, id):
        admin = cls.query.filter_by(id=id).first()
        db.session.delete(admin)
        db.session.commit()


@dataclass
class Category(db.Model):
    __tablenamee__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def getAllCategory(cls):
        return cls.query.all()

    @classmethod
    def getCategoryById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def addCategory(cls, name):
        category = cls(name=name)
        db.session.add(category)
        db.session.commit()

    @classmethod
    def updateCategory(cls, id, name):
        admin = cls.query.filter_by(id=id).first()
        admin.username = name
        db.session.commit()

    @classmethod
    def deleteCategory(cls, id):
        admin = cls.query.filter_by(id=id).first()
        db.session.delete(admin)
        db.session.commit()


@dataclass
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    discountPrice = db.Column(db.Float)
    categoryId = db.Column(db.Integer, db.ForeignKey("category.id"))

    def __init__(self, id, name, description, price, discountPrice, categoryId):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.discountPrice = discountPrice
        self.categoryId = categoryId

    @classmethod
    def getAllProducts(cls):
        return cls.query.all()

    @classmethod
    def getProductById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def addProduct(cls,name, description, price, discountPrice,categoryId):
        product = cls(name=name,description=description,price=price,discountPrice=discountPrice,categoryId=categoryId)
        db.session.add(product)
        db.session.commit()

    @classmethod
    def updateProduct(cls, id, name, description, price, discountPrice,categoryId):
        product = cls.query.filter_by(id=id).first()
        product.name = name
        product.description = description
        product.price = price
        product.discountPrice = discountPrice
        product.categoryId=categoryId
        db.session.commit()

    @classmethod
    def deleteProduct(cls, id):
        product = cls.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()
