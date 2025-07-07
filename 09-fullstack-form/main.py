from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
    user="root",
    password="huzair321",
    database="office",
    host="127.0.0.1"
)

@app.route("/getEmployees")
def get_emplyees():
    cursor = db_connection.cursor()
    cursor.execute("select * from employees")
    employees = cursor.fetchall()
    employee = [{"name":emp[0], "position":emp[1]} for emp in employees]
    return {"employee":employee}

app.run(debug=True)