from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

# everytime this is called a new instance of the Flask app is created
def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('settings.py')
    
    db.init_app(app)
    
    from user.views import user_app
    app.register_blueprint(user_app)
    
    return app
    