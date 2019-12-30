#tutorial from https://www.codeproject.com/Articles/1255416/Simple-Python-Flask-Program-with-MongoDB?msg=5626151#xx5626151xx

from flask import Flask, render_template,request,redirect,url_for # For flask implementation

from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    #initialize the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    #initialize plugins
    mongo.init_app(app = app)


    with app.app_context():
        from . import views

    return app