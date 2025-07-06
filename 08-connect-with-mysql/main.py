# import flask to create a server an jsonify to return a json object
from flask import Flask, jsonify

# import mysql.connector, this will establish a connection between your python code and mysql
import mysql.connector

# create a flask instance
app = Flask(__name__)

# create a database connections usong connect functions
# this will take some kwargs, you see details about those kwargs at:
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html 
db_connection = mysql.connector.connect(
    user="your username", # e.g. root
    password="your password", # e.g. 123
    database="your database name", # e.g office
    host="hosting/domain" # e.g localhost or your domain name
    )


@app.route("/getTable", methods=["GET"])
def get_table():
    cursor = db_connection.cursor()
    
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    db_connection.close()
    
    tables = [table[0] for table in tables]
    return jsonify({"tables":tables}), 200

app.run(debug=True)