from flask import Flask, redirect, request, Response, url_for, session

app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "123":
            session["   "] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again!", mimetype="text/plain")
            
    return"""
    <h2>Login Page</h2>
    <form method="POST"> 
    Username: <input type="text" name="username">
    Password: <input type="text" name="password">
    <input type="submit" value="Login">
    </form>
    
"""

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome, {session['user']}!</h2>
        <a href={url_for('logout')}>Logout</a>
        """
    return redirect(url_for("login"))    

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    