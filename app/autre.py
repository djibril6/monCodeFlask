from flask import Flask, render_template
import pymysql

app = Flask(__name__)

app.config.from_object('config')

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "admin"
        password = "admin"
        db = "nakoabase"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self):
        self.cur.execute("SELECT * FROM market_fournisseur")
        result = self.cur.fetchall()
        return result

@app.route('/')
def index():
	t = Database()
	res = t.list_employees()
	return render_template('index.html', result=res, content_type='application/json')
    #return "Hello world !"

if __name__ == "__main__":
    app.run()