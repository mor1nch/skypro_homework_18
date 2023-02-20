from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.director import DirectorSchema, Director

director_ns = Namespace("director")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
