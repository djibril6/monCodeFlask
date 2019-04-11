from flask import Flask, render_template, request, redirect, session, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import pymysql
import hashlib
from datetime import date
from .models import *

#

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')
cors = CORS(app, resources={r"/serviceapi/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

class ServiceApi(Resource):
	def post(self):
		# lors de l'envoi d'une requête post
		mode = request.form.get("mode")
		if mode == "login":
			# Tentative de connexion
			tel = request.form.get("tel")
			mdp = hashlib.sha224(request.form.get("mdp").encode('utf8')).hexdigest()

			
			user = User.query.filter_by(tel=tel, password=mdp)
	
			user2 = UserSchema(many=True)
			user = user2.dump(user).data

			if user:
				return {'success': True, 'message': 'Bienvenu !', 'result': user}
			else:
				return {'success': False, 'message': 'Téléphone ou mot de passe incorrect'}
		elif mode == "modif":
			# Modification de compte
			theId = request.form.get("id")
			newmdp = request.form.get("newmdp")
			oldmdp = request.form.get("oldmdp")
			nom = request.form.get("nom")
			prenom = request.form.get("prenom")
			tel = request.form.get("tel")
			email = request.form.get("email")

			try:
				element = User.query.get(theId)
			except Exception as e:
				return {'success': False, 'message': 'Une erreur est survenue !'}

			if oldmdp != element.password:
				return {'success': False, 'message': 'Une erreur est survenue !'}

			if newmdp:
				newmdp = hashlib.sha224(newmdp.encode('utf8')).hexdigest()
				element.password = newmdp

			element.nom = nom
			element.prenom = prenom
			element.tel = tel
			element.email = email
			try:
				db.session.commit()
				return {'success': True, 'message': 'Modifé avec succès !'}
			except Exception as e:
				return {'success': False, 'message': 'Une erreur est survenue !'}
		elif mode == "del":
			#Suppression de compte
			theId = request.form.get("id")	

			#On vérifie si ce n'est pas le seul compte root de la base de données
			allUser = User.query.filter_by(compte="root")
			i = 0;
			for x in allUser:
				i+=1
			if i <= 1:
				return {'success': False, 'message': "Vous ne pouvez pas le supprimer car il s'agit du seul root compte actif"}
			try:
				element = User.query.get(theId)
				db.session.delete(element)
				db.session.commit()
				return {'success': True, 'message': 'Supprimé avec succès !'}
			except Exception as e:
				return {'success': False, 'message': 'Une erreur est survenue !'}

#Chemin 
api.add_resource(ServiceApi, '/serviceapi/')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])


@app.route('/', methods=['POST', 'GET'])
def login():
	success = False
	if request.form:
		tel = request.form.get("tel")
		mdp = hashlib.sha224(request.form.get("mdp").encode('utf8')).hexdigest()

		user = User.query.filter_by(tel=tel, password=mdp).first()

		if user:
			if user.compte == "root":
				session['telUser'] = user.tel
				return redirect("/home/")

	if request.args.get("logout") == "oui":
		session.pop('telUser', None)
	return render_template('login.html')

@app.route('/home/', methods=['POST', 'GET'])
def home():
	success = False
	if request.form:
		mot_defaut = "pass"
		mdp = hashlib.sha224(mot_defaut.encode('utf8')).hexdigest()
		nom = request.form.get("nom")
		prenom = request.form.get("prenom")
		tel = request.form.get("tel")
		email = request.form.get("email")
		dateAjout = date.today()
		compte = "normal"
		if request.form.get("admin") == "on":
			compte = "root"

		try:
			user = User(nom=nom, prenom=prenom, tel=tel, email=email, date_inscription=dateAjout, password=mdp, compte=compte)
			db.session.add(user)
			db.session.commit()
			success = True
		except Exception as e:
			print("Erreur survenue lors de l'ajout")

	if request.args.get("sup") == "oui":
		theId = request.args.get("id")
		try:
			element = User.query.get(theId)
			db.session.delete(element)
			db.session.commit()
		except Exception as e:
			print("Erreur survenue lors de la suppression")

	

	user = User.query.all()
	if "telUser" in session:
		return render_template('home.html', result=user, success=success)
	else:
		return redirect("/")

if __name__ == "__main__":
    app.run()