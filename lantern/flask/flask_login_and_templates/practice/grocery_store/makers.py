from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Server, Manager

from grocery_store.config import Config
from grocery_store.routes import users, goods, stores, auth
from grocery_store.db import db
from grocery_store.commands import Populate


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(goods)
    app.register_blueprint(stores)
    app.register_blueprint(auth)
    return app


def make_db(app):
    db.init_app(app)
    return db


def make_manager(app):
    manager = Manager(app)
    manager.add_command('runserver', Server(host=Config.HOST, port=Config.PORT))
    manager.add_command('db', MigrateCommand)
    manager.add_command('populate', Populate)
    return manager
