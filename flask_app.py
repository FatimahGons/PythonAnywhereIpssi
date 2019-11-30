"""This is an application that will allow you to add a comment with a username."""

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask(__name__)
app.config["DEBUG"] = True

DB_DATABASE = SQLAlchemy(app)

SQLALCHEMY_DATABASE_URI = \
"mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="FatimahGs",
    password="loicfaty",
    hostname="FatimahGs.mysql.eu.pythonanywhere-services.com",
    databasename="FatimahGs$PythonTwitter",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB_DATABASE.create_all()

class MyTweet(DB_DATABASE.Model):
    """Adding a new table MyTweet to the database."""
    __tablename__ = 'MyTweet'
    id = Column(Integer, primary_key=True)
    fistname = Column(String(20))
    message = Column(String(280))

class MyAddressIP(DB_DATABASE.Model):
    """Adding a new table MyAddressIP to the database."""
    __tablename__ = 'MyAddressIP'
    id = Column(Integer, primary_key=True)
    ip = Column(String(20))

@app.after_request
def add_header(response):
    """Adding a header to the application."""
    header = response.headers
    response.cache_control.max_age = 300
    header['Access-Control-Allow-Origin'] = [
        '195.154.176.62',
        '80.15.154.187'
    ]
    return response

def add_message(message_parameter):
    """This function allows a user to add a message and add the data into MyTweet table."""
    content = MyTweet(
        fistname=message_parameter["user-name"],
        message=message_parameter["user-text"]
    )
    DB_DATABASE.session.add(content)
    DB_DATABASE.session.commit()

def add_ip(my_ip):
    """This function's add an IP address into MyAddressIP table."""
    content_ip = MyAddressIP(
        ip=my_ip,
    )
    DB_DATABASE.session.add(content_ip)
    DB_DATABASE.session.commit()

def get_messages():
    """Get all the messages from MyTweet table."""
    mes_tweets = MyTweet.query.all()
    return mes_tweets

def get_ip():
    """Get all the IP address from MyAddressIP table."""
    my_ip = MyAddressIP.query.all()
    return my_ip

@app.route('/')
def home():
    """Return a welcome message."""
    return 'Bienvenue !'

@app.route('/login')
def login():
    """Return an html template with login fields."""
    return render_template('login.html')

@app.route('/signup')
def signup():
    """Return a message."""
    return 'signup'

@app.route('/logout')
def signout():
    """Return a message."""
    return 'logout'

@app.route('/timeline/<username>/')
def display_tweet_by_username(username):
    """Display all the tweets by the user's name."""
    tab_user_tweet = []
    user_tweet_name = username
    mes_tweets = get_messages()
    for un_tweet in mes_tweets:
        if un_tweet.fistname == username:
            tab_user_tweet.append(un_tweet)
    return render_template("usernameTweet.html", \
    tab_user_tweet=tab_user_tweet, user_tweet_name=user_tweet_name)

def ipa():
    """Returned the ip address of the user that posted a message."""
    ip_address = request.headers['X-Forwarded-For']
    return ip_address

@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """Processing data in order to find which data to add into the database."""
    user_ip = ipa()
    my_ips = get_ip()
    forbidden_word = "barre"
    if request.method == 'POST':
        if len(request.form['user-name']) <= 20 and \
        len(request.form['user-text']) <= 280 and \
        forbidden_word not in request.form['user-name'] and \
        forbidden_word not in request.form['user-text']:
            if not my_ips:
                found = False
                for i in my_ips:
                    if i.ip == user_ip:
                        return "Adresse IP existante"
                        found = True
                        break
                if found is False:
                    add_ip(user_ip)
            else:
                add_ip(user_ip)
            add_message(request.form)
            return redirect(url_for('timeline'))
        else:
            return "Votre message est trop long ou contient le mot interdit"
    if request.method == 'GET':
        return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
    """Display all the data from the database."""
    gaz = get_messages()
    return render_template("timeline.html", gaz=gaz)
