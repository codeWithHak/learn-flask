from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")





