from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/feedback",methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")
        
        return render_template("thankyou.html", username=username, message=message)
    
    return render_template("feedback.html")