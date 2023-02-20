from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.movie import MovieSchema, Movie

movies_ns = Namespace("movie")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
