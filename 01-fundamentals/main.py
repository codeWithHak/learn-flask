from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return"Hello Flasssssk"

products_data = [
    {'name':'floor','price':'140','quantity':'200'},
    {'name':'rice','price':'220','quantity':'150'},
    {'name':'sugar','price':'240','quantity':'100'}
    ]

@app.route("/products")
def products():
    output = ''
    for product in products_data:
        output += f"Name: {product['name']} Price:{product['price']} Quantity Available:{product['quantity']} <br><br>"
    return output

@app.route("/submit", methods=["POST","GET"])
def submit():
    if request.method == "POST":
        return "You posted some data!!!"
    else:
        return "You recieved data"