import mysql.connector as connector
import json
import os

from storage import bot_storage

# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor()


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

cursor.execute('ALTER TABLE users MODIFY income TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
connection.commit()

cursor.execute('ALTER TABLE users MODIFY expense TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
connection.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS operations
(
    operation_id INTEGER UNIQUE PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    operation_type TEXT NOT NULL,
    currency TEXT NOT NULL,
    category TEXT NOT NULL,
    value FLOAT NOT NULL
);''')
connection.commit()


def check_user(user_id: int):
    cursor.execute('SELECT user_id FROM users WHERE user_id = %s', (user_id, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


def create_user(user_id: int):
    user_id: int = bot_storage[user_id]['user_id']
    username: str = bot_storage[user_id]['username']
    currency: str = bot_storage[user_id]['currency']
    balance: float = bot_storage[user_id]['balance']
    income: dict = bot_storage[user_id]['income']
    expense: dict = bot_storage[user_id]['expense']

    cursor.execute('''INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s);''',
                   (user_id, username, currency, balance, json.dumps(income, ensure_ascii=False), json.dumps(expense, ensure_ascii=False)))
    connection.commit()


def fetch_income_categories(user_id: int) -> dict:
    cursor.execute('SELECT income FROM users WHERE user_id = %s', (user_id, ))
    return json.loads(cursor.fetchall()[0][0])