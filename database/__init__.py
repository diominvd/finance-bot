import mysql.connector as connector
import os


# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor(buffered=True)

def db_connect(func):
    def wrapper(*args, **kwargs):
        connection.ping(reconnect=True)
        return func(*args, **kwargs)
    return wrapper


cursor.execute('''CREATE TABLE IF NOT EXISTS users
(
    user_id INTEGER UNIQUE PRIMARY KEY,
    username TEXT NOT NULL,
    currency TEXT NOT NULL,
    balance FLOAT NOT NULL,
    income JSON NOT NULL,
    expense JSON NOT NULL
);''')
connection.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS operations
(
    operation_id INTEGER UNIQUE PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    operation_type TEXT NOT NULL,
    currency TEXT NOT NULL,
    category TEXT NOT NULL,
    value FLOAT NOT NULL,
    date TEXT NOT NULL
);''')
connection.commit()