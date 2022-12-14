from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String(50),unique=True)
    phoneNumber=db.Column(db.String(15))
    password=db.Column(db.String(15))

    def __repr__(self):
        return f"name: {self.name} email: {self.email} phoneNumber:{self.phoneNumber}"