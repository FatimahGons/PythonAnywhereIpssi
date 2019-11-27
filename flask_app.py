from flask import Flask, request, render_template, redirect, url_for
import csv
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'FatimahGs.mysql.eu.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'FatimahGs'
app.config['MYSQL_PASSWORD'] = 'loicfaty'
app.config['MYSQL_DB'] = 'PythonTwitter'

mysql = MySQL(app)

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		details = request.form
        username = details['user-name']
		print("username")
		print(username)
        message = details['user-text']
		cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyTweet(username, message) VALUES (%s, %s)", (username, message))
        mysql.connection.commit()
        cur.close()
		dump_to_csv(request.form)
		return redirect(url_for('timeline'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	return render_template("timeline.html", gaz = gaz)

def parse_from_csv():
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)