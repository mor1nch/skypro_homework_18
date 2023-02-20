from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.genre import GenreSchema, Genre

director_ns = Namespace("authors")
director_schema = GenreSchema()
directors_schema = GenreSchema(many=True)
