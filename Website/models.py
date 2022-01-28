from . import db

class User(db.Document): #MongoEngine uses Document which has its own collection in the database, which is created by inheriting from mongoengine.Document
    name = db.StringField()
    email = db.StringField()
    password1 = db.StringField(required = True)
    password2 = db.StringField(required = True)

    def json_data(self):
        return{
            "name": self.name,
            "email": self.email,
            "password1": self.password1,
            "password2": self.password2
        }