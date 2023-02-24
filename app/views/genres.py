from flask import jsonify
from flask_restx import Resource, Namespace
from app.dao.models.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace("genre")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return jsonify(genres_schema.dump(all_genres)), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return jsonify(genre_schema.dump(genre)), 200
