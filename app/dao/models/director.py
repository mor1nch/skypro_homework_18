from marshmallow import Schema, fields
from app.setup_db import db


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer)
    name = db.Column(db.String)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
