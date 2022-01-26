# this file allows contents to be imported for the website 
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'absgdhcj' #secret_key is used for authentication purpose especially, for sessions and cookies

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app