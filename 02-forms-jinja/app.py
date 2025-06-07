from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student():
    return render_template(
        "student.html",
        name="Huzair",
        is_topper=True,
        subjects=["Eng","Isl","Pst"]
    )

