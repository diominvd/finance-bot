import mysql.connector as connector
import os


# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor()

# Database -> users.
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY UNIQUE,
    products FLOAT,
    cafes FLOAT,
    auto FLOAT,
    transport FLOAT,
    home FLOAT,
    entertainment FLOAT,
    sport FLOAT,
    health FLOAT,
    education FLOAT,
    gifts FLOAT,
    beauty FLOAT,
    clothes FLOAT,
    technic FLOAT,
    subscriptions FLOAT,
    total FLOAT);''')
connection.commit()

# Database -> operations.
cursor.execute('''CREATE TABLE IF NOT EXISTS operations(
    operation_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    user_id INT,
    category TEXT,
    value FLOAT,
    date TEXT);''')
connection.commit()