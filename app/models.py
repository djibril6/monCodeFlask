from flask_sqlalchemy import SQLAlchemy

from .views import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(60), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(80), nullable=True)
    date_inscription = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, nom, prenom, tel, email, compte, password):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.compte = compte
        self.password = password

db.create_all()