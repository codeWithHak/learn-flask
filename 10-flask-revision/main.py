from flask import Flask, request, redirect, session, url_for, render_template
import mysql.connector

db_connection = mysql.connector.connect(
    user="root",
    password="huzair321",
    database="office",
    host="127.0.0.1"
)

app = Flask(__name__)
app.secret_key = "123"
#1 basic get request
users:dict={}

@app.route("/getUsers")
def get_users():
    return users

#2 basic auth
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        session["user"] = email
        print("user")
        print(session)
        return redirect(url_for("login"))
    return render_template('signup.html')



@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email] == password:
            session["user"] = email
            return render_template("welcome.html")
        
        return render_template("signup.html")
    return render_template("login.html")

app.run(debug=True)