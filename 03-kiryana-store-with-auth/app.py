from flask import Flask, request, render_template, redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "my_secret"

users_data={}

inventory=[
    {'name':"floor", "price":'120', "available":"200"},
    {'name':"rice", "price":'220', "available":"100"},
    {'name':"soap", "price":'90', "available":"300"},
    {'name':"oil", "price":'500', "available":"250"},
]


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        age = request.form.get("age")
        gender = request.form.get("gender")

        users_data[username] = password
        
        return redirect(url_for('login'))
    
    return render_template("signup.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in users_data and users_data[username] == password:
            session['user'] = username
            return redirect(url_for("shop"))
        
        else:
            return Response("Invalid credentials",mimetype="text/plain")
            
    
    return render_template("login.html")

@app.route("/shop")
def shop():
    return render_template("shop.html", inventory=inventory)

@app.route("/users")
def users():
    return render_template("users.html", users_data=users_data)