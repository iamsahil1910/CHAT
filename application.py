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
    db.execute("INSERT INTO users (fname, lname, email, gender, password) VALUES(:fname, :lname, :email, :gender, :password)", {"fname":fname, "lname":lname, "email":email, "gender":gender, "password":pwd})
    db.commit()

    n = db.execute("SELECT fname FROM users WHERE email = :email", {"email":email    }).fetchone()
    return render_template("home.html", user = n[0])

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    email = request.form.get("email")
    password = request.form.get("pwd")
    if db.execute("SELECT user FROM users WHERE email = :email AND password = :password", {"email": email, "password": password}).rowcount == 0:
        return render_template("login.html")
    else:
        n = db.execute("SELECT fname FROM users WHERE email = :email", {"email": email}).fetchone()
        return render_template("home.html", user=n[0])
