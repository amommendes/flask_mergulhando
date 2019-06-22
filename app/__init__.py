import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1:3306/mergulhando",
        SQLALCHEMY_ECHO=True,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.models.orm import db 
    app.app_context().push()
    db.init_app(app)
    db.engine.execute("create database if not exists mergulhando;")
    db.create_all()
    
    from . import auth
    app.register_blueprint(auth.bp)

    from . import user_api
    api.add_resource(user_api.RegisterUser, "/user")
    api.add_resource(user_api.RegisterPresence, "/class/register")

    from . import home
    app.register_blueprint(home.bp)

    return app