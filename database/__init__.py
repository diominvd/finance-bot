import mysql.connector as connector
import os


# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor()


cursor.execute('''CREATE TABLE users
(
    user_id INTEGER UNIQUE,
    username TEXT,
    currency TEXT,
    income JSON NOT NULL,
    expense JSON NOT NULL
);''')
connection.commit()

cursor.execute('''CREATE TABLE operations
(
    operation_id INTEGER UNIQUE AUTO_INCREMENT,
    user_id INTEGER,
    operation_type TEXT,
    currency TEXT,
    category TEXT,
    value FLOAT
);''')
connection.commit()