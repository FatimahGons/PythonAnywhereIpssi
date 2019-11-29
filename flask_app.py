from flask import Flask, request, render_template, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

db = SQLAlchemy(app)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="FatimahGs",
    password="loicfaty",
    hostname="FatimahGs.mysql.eu.pythonanywhere-services.com",
    databasename="FatimahGs$PythonTwitter",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.create_all()

class MyTweet(db.Model):
    __tablename__ = 'MyTweet'
    id = db.Column(db.Integer, primary_key=True)
    fistname = db.Column(db.String(20))
    message = db.Column(db.String(280))

class MyAddressIP(db.Model):
    __tablename__ = 'MyAddressIP'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20))

@app.after_request
def add_header(response):
    header = response.headers
    response.cache_control.max_age = 300
    header['Access-Control-Allow-Origin'] = [
        '195.154.176.62',
        '80.15.154.187'
    ]
    return response

def addMessage(d):
    content = MyTweet(
        fistname=d["user-name"],
        message=d["user-text"]
    )
    db.session.add(content)
    db.session.commit()

def addIP(my_ip):
    contentIP = MyAddressIP(
        ip=my_ip,
    )
    db.session.add(contentIP)
    db.session.commit()

def getMessages():
    mes_tweets = MyTweet.query.all()
    return mes_tweets

def getIP():
    my_ip = MyAddressIP.query.all()
    return my_ip

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/profile')
def profile():
    return 'profile'

#auth = Blueprint('auth', __name__)

@app.route('/login')
def login():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/signup')
def signup():
    return 'signup'

@app.route('/logout')
def signout():
    return 'logout'

@app.route('/timeline/<username>/')
def test(username):
    tab_user_tweet = []
    user_tweet_name = username
    mes_tweets = getMessages()
    for unTweet in mes_tweets:
        if unTweet.fistname == username:
            tab_user_tweet.append(unTweet)
    return render_template("usernameTweet.html", tab_user_tweet=tab_user_tweet, user_tweet_name=user_tweet_name)

def ipa():
    ip_address = request.headers['X-Forwarded-For']
    return ip_address

@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    user_ip = ipa()
    my_ips = getIP()
    forbiddenWord = "barre"
    if request.method == 'POST':
        if len(request.form['user-name']) <= 20 and len(request.form['user-text']) <= 280 and forbiddenWord not in request.form['user-name'] and forbiddenWord not in request.form['user-text']:
            if len(my_ips) > 0:
                found = False
                for i in my_ips:
                    if i.ip == user_ip:
                        return "Adresse IP existante"
                        found = True
                        break
                if found is False:
                    addIP(user_ip)
            else:
                addIP(user_ip)
            addMessage(request.form)
            return redirect(url_for('timeline'))
        else:
            return "Votre message est trop long ou contient le mot interdit"
		#return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
    gaz = getMessages()
    return render_template("timeline.html", gaz=gaz)