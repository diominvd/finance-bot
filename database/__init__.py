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


def fetch_user_currency(user_id: int) -> str:
    cursor.execute('SELECT currency FROM users WHERE user_id = %s', (user_id, ))
    return cursor.fetchall()[0][0]


def load_categories(user_id: int, operation_type: str) -> dict:
    match operation_type:
        case 'income':
            cursor.execute('SELECT income FROM users WHERE user_id = %s', (user_id, ))
            categories: dict = json.loads(str(cursor.fetchall()[0][0]))

            return categories
        case 'expense':
            cursor.execute('SELECT expense FROM users WHERE user_id = %s', (user_id,))
            categories: dict = json.loads(str(cursor.fetchall()[0][0]))

            return categories


def add_operation(user_id: int, operation_type: str) -> None:
    # Fetch operation data from bot storage.
    user_id: int = bot_storage[user_id]['user_id']
    operation_type: str = operation_type
    currency: str = bot_storage[user_id]['currency']
    category: str = bot_storage[user_id]['category']
    value: float = bot_storage[user_id]['value']

    # Add operation in database/operations.
    cursor.execute('''INSERT INTO operations (user_id, operation_type, currency, category, value) VALUES(%s, %s, %s, %s, %s);''',
                   (user_id, operation_type, currency, category, value))
    connection.commit()

    # Add operation in database/users.
    if operation_type == 'income':
        # Load income categories.
        cursor.execute('SELECT income FROM users WHERE user_id = %s', (user_id, ))
        income_categories: dict = json.loads(str(cursor.fetchall()[0][0]))

        # Update data in categories.
        income_categories[category]['value'] += value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET income = %s, balance = balance + %s WHERE user_id = %s', (json.dumps(income_categories, ensure_ascii=False), value, user_id))
        connection.commit()
    elif operation_type == 'expense':
        # Load income categories.
        cursor.execute('SELECT expense FROM users WHERE user_id = %s', (user_id,))
        expense_categories: dict = json.loads(str(cursor.fetchall()[0][0]))

        # Update data in categories.
        expense_categories[category]['value'] += value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET expense = %s, balance = balance - %s WHERE user_id = %s', (json.dumps(expense_categories, ensure_ascii=False), value, user_id))
        connection.commit()