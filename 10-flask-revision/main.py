from flask import Flask, request, redirect, session, url_for, render_template
import mysql.connector

db_connection = mysql.connector.connect(
    user="root",
    password="huzair321",
    database="users",
    host="127.0.0.1"
)

app = Flask(__name__)
app.secret_key = "123"
#1 basic get request
# users=["huzair","huzaifa","khizar"]

# @app.route("/getUsers")
# def get_users():
#     return users


#2 basic auth
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        cursor = db_connection.cursor()
        cursor.execute(f"""INSERT INTO all_users2 (email,password)
                       VALUES('{email}','{password}')""")
        db_connection.commit()
        # users = cursor.fetchall()
        # user = [u[0] for u in users]

        
        return redirect(url_for("login"))
    return render_template('signup.html')



@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        cursor = db_connection.cursor(dictionary=True)

        cursor.execute(f"SELECT password FROM all_users2 WHERE email = '{email}'")
        users = cursor.fetchone()
        

        if users["password"] == password:
            session["user"] = email 
            return render_template("welcome.html")
        else:
            return "Invalid email or password", 401


    # return render_template("signup.html")
    return render_template("login.html")

app.run(debug=True)