from flask import Flask, render_template
import pymysql

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
	return render_template('index.html', content_type='application/json')
    #return "Hello world !"

if __name__ == "__main__":
    app.run()