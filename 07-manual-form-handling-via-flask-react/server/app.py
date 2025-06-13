from flask import Flask, request, jsonify
from flassk-cors importCORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def feedback():
    if request.mthod == "POST":
        data = form.get_json()
        name = data.get("name")
        message = data.get("message")

    