from flask import request
from flask_restx import Resource, Namespace
from app.setup_db import db
from app.dao.models.director import DirectorSchema, Director

director_ns = Namespace("authors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
