# Simple Flask MySQL Connection Example
# This shows how to connect Python with MySQL database

# Step 1: Import the libraries we need
from flask import Flask, jsonify  # Flask for web server, jsonify for JSON responses
import mysql.connector  # This connects Python to MySQL database

# Step 2: Create Flask app
app = Flask(__name__)

# Step 3: Setup database connection
# Replace these with your actual database details
connection = mysql.connector.connect(
    host='localhost',        # Where your MySQL server is running
    user='root',            # Your MySQL username
    password='your_password', # Your MySQL password
    database='your_database' # Your database name
)

# Step 4: Create an API endpoint
@app.route('/getTables', methods=['GET'])
def get_tables():
    # Create a cursor this lets us execute SQL commands
    cursor = connection.cursor()
    
    # Execute SQL command to show all tables, (you can execute any sql command here)
    cursor.execute("SHOW TABLES")
    
    # fetch all rows (result will be in a list of tuples)
    tables = cursor.fetchall()
    
    # Close the cursor (good practice)
    cursor.close()
    
    # Convert results to a simple list
    # tables comes as list of tuples like:[(table1,), (table2,)] so we extract just the names
    table_names = [table[0] for table in tables]
    
    # Return as JSON
    return jsonify(table_names)

# Step 5: Run the app
if __name__ == '__main__':
    app.run(debug=True)  # debug=True shows errors clearly