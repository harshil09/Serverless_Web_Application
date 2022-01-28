# this file allows contents to be imported for the website 
from flask import Flask
from flask_mongoengine import MongoEngine

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'absgdhcj' #secret_key is used for authentication purpose especially, for sessions and cookies
    app.config['MONGODB_SETTINGS'] = {
        'db': 'user',
        'host': 'localhost',
        'port': 27017
    }
    app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/db_name'
}
    db = MongoEngine() #initialized mongodb object
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app