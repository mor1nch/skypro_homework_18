from flask import request, jsonify
from flask_restx import Resource, Namespace
from app.dao.models.movie import MovieSchema
from app.implemented import movie_service

movies_ns = Namespace("movie")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        req_director_id = request.values.get('director_id')
        req_genre_id = request.values.get('genre_id')
        req_year = request.values.get('year')

        if req_director_id is None and req_genre_id is None and req_year is None:
            all_movies = movie_service.get_all()
            return jsonify(movies_schema.dump(all_movies)), 200
        elif req_director_id is not None:
            movies_by_director = movie_service.get_all_by_director(req_director_id)
            return jsonify(movies_schema.dump(movies_by_director)), 200
        elif req_director_id is not None:
            movies_by_genre = movie_service.get_all_by_genre(req_genre_id)
            return jsonify(movies_schema.dump(movies_by_genre)), 200
        elif req_year is not None:
            movies_by_year = movie_service.get_all_by_year(req_year)
            return jsonify(movies_schema.dump(movies_by_year)), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "Фильм успешно добавлен", 201


@movies_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "Фильм успешно обновлён", 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "Фильм успешно удалён", 204
