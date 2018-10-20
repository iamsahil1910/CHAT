from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    gender = request.form.get("gender")
    pwd = request.form.get("pwd")
    if not fname or not lname or not email or not pwd:
        return render_template("signup.html")
    return render_template("home.html")
