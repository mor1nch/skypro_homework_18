from marshmallow import Schema, fields
from app.setup_db import db


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
