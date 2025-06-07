from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")
