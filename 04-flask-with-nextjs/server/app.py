from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/api/home")
def return_home():
    return jsonify({
        "message":"Hello NextJs + Flask Babbyyyyy",
        "people":["Huzair","Huzaifa","Aaa merii jaaan"]
    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)