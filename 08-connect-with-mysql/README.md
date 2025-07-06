# How to Connect MySQL with Python

## What is this?

This guide shows you how to connect a MySQL database with Python using Flask. If you just learned Python and want to work with databases, this is perfect for you!

## What you'll learn

- How to connect Python to MySQL
- How to run SQL commands from Python
- How to create a simple web API that shows database data

## What you need before starting

1. **Python installed** on your computer
2. **MySQL installed** and running
3. **A MySQL database** with some tables (any database works for testing)

## Step 1: Install required packages

Open your terminal/command prompt and run:

```bash
pip install flask mysql-connector-python
```

**What these do:**
- `flask`: Creates web servers with Python
- `mysql-connector-python`: Connects Python to MySQL databases

## Step 2: Set up your database

Make sure you have:
- MySQL server running
- A database created (any name is fine)
- Your MySQL username and password ready

## Step 3: Create the Python file

Create a file called `app.py` and copy the code from the example above.

**Important:** Change these lines in the code:
```python
host='localhost',        # Change if MySQL is on another computer
user='root',            # Change to your MySQL username
password='your_password', # Change to your MySQL password
database='your_database' # Change to your database name
```

## Step 4: Run your application

In terminal, go to your project folder and run:

```bash
python app.py
```

You should see something like:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

## Step 5: Test it

Open your web browser and go to:
```
http://localhost:5000/tables
```

You should see a list of all tables in your database displayed as JSON!

## How it works

### The Connection
```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='your_database'
)
```
This creates a bridge between Python and MySQL.

### The Cursor
```python
cursor = connection.cursor()
```
A cursor is like a pointer that lets you execute SQL commands.

### Executing SQL
```python
cursor.execute("SHOW TABLES")
```
This runs the SQL command `SHOW TABLES` which lists all tables.

### Getting Results
```python
tables = cursor.fetchall()
```
This gets all the results from the SQL command.

### Converting to JSON
```python
return jsonify(table_names)
```
This converts Python data to JSON format for web browsers.

## Common Issues

**"Access denied" error:**
- Check your username and password are correct

**"Can't connect to MySQL server":**
- Make sure MySQL is running
- Check if `host='localhost'` is correct

**"Unknown database":**
- Make sure the database name exists in MySQL

## What's next?

Once this works, you can:
1. Try different SQL commands like `SELECT * FROM table_name`
2. Add more API endpoints
3. Learn about inserting and updating data

## Complete File Structure

I'm using UV (pip's replacement) so my project structure is a bit different but if you are using pip,
Your project should look like this:
```
my-project/
├── app.py          # Your main Python file
└── README.md       # This guide
```

That's it! You've successfully connected MySQL with Python!