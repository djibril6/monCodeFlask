from flask import Flask, render_template
import pymysql

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def login():
	return render_template('login.html', content_type='application/json')

@app.route('/home/', methods=['POST', 'GET'])
def home():
	return render_template('home.html')

if __name__ == "__main__":
    app.run()