from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.movie import MovieSchema, Movie

director_ns = Namespace("authors")
director_schema = MovieSchema()
directors_schema = MovieSchema(many=True)
