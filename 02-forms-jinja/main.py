from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/submit",methods=["GET","POST"])
def welcome():
    
       if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "123":
            return render_template("welcome.html", name=username)
        else:
            return Response("Invalid Credentials", mimetype="text")
    
    
    