from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from create_data import create_data

from views.movies import movies_ns
from views.genres import genre_ns
from views.directors import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(app, db)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
