from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.genre import GenreSchema, Genre

genre_ns = Namespace("genre")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
