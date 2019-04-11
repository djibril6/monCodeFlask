# monCodeFlask

# Installer les dépendances contenues dans le fichier requirements.txt
```bash
pip3 install -r requirements.txt
```
## Exporter la base de données dans un serveur mysql (fichier flask.sql)

## Aller dans le fichier config.py pour adapter les données de connexion à votre serveur mysql (variable SQLALCHEMY_DATABASE_URI)

## Dans le fichier run.py, modifer la première ligne en fonction du chemin vers l'interpreteur de python de votre machine

## Aller dans le répertoire du projet puis lancer le serveur
```bash
python3.6 run.py
```

Code d'application web de gestion d'authetification + REST API communiquant avec une appli mobile IONIC<br>
<br>
Base de données MySQL utilsé<br>
Deux comptes sont présents dans la base de données<br>
Se connecter avec le compte : <br>
tel : 80686719<br>
mot de passe : pass<br>
seuls les comptes root ont accès à l'application Web<br>
les comptes sont créés avec un mot de passe par défaut (pass) qui peut être changé via l'application mobile
