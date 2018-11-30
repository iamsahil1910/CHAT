import os

from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://sahil:tivnoloitb@localhost:5432/sahil')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    gender = request.form.get("gender")
    pwd = request.form.get("pwd")
    if not fname or not lname or not email or not pwd:
        return render_template("signup.html")
    return render_template("home.html")
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    username = request.form.get("email")
    password = request.form.get("pwd")
    if db.execute("SELECT user FROM users WHERE email = :username AND password = :password", {"username": username, "password": password}).rowcount == 0:
        return render_template("login.html")
    else:
        n = db.execute("SELECT fname FROM users WHERE email = :username", {"username": username}).fetchall()
        return render_template("home.html", user=n)
