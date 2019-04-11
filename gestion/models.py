from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, pre_load, validate


app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(60), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=True)
    date_inscription = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    compte = db.Column(db.String(6), nullable=False)

    def __init__(self, nom, prenom, tel, email, date_inscription, password, compte):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.date_inscription = date_inscription
        self.password = password
        self.compte = compte

class UserSchema(ma.Schema):
    id = fields.Integer(required=True)
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    tel = fields.String(required=True)
    email = fields.String(required=False)
    date_inscription = fields.Date()
    password = fields.String(required=True)
    compte = fields.String(required=True)
        

#db.create_all()