import mysql.connector as connector
import json
import os

from storage import bot_storage

# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor(buffered=True)


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
    value FLOAT NOT NULL,
    date TEXT NOT NULL
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
    date: str = bot_storage[user_id]['date']

    # Add operation in database/operations.
    cursor.execute('''INSERT INTO operations (user_id, operation_type, currency, category, value, date) VALUES(%s, %s, %s, %s, %s, %s);''',
                   (user_id, operation_type, currency, category, value, date))
    connection.commit()

    # Add operation in database/users.
    if operation_type == 'income':
        # Load income categories.
        cursor.execute('SELECT income FROM users WHERE user_id = %s', (user_id, ))
        income_categories: dict = load_categories(user_id, operation_type='income')

        # Update data in categories.
        income_categories[category]['value'] += value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET income = %s, balance = balance + %s WHERE user_id = %s', (json.dumps(income_categories, ensure_ascii=False), value, user_id))
        connection.commit()
    elif operation_type == 'expense':
        # Load income categories.
        cursor.execute('SELECT expense FROM users WHERE user_id = %s', (user_id,))
        expense_categories: dict = load_categories(user_id, operation_type='expense')

        # Update data in categories.
        expense_categories[category]['value'] += value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET expense = %s, balance = balance - %s WHERE user_id = %s', (json.dumps(expense_categories, ensure_ascii=False), value, user_id))
        connection.commit()


def load_profile_info(user_id: int) -> tuple:
    cursor.execute('SELECT username, currency, balance FROM users WHERE user_id = %s', (user_id, ))
    return cursor.fetchall()[0]


def load_last_operations(user_id: int) -> list:
    cursor.execute('SELECT operation_type, currency, category, value, date FROM operations WHERE user_id = %s LIMIT 10', (user_id, ))
    return cursor.fetchall()


def delete_last_operation(user_id: int) -> None:
    # Fetch last operation data.
    cursor.execute('SELECT operation_type, category, value FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1', (user_id, ))
    data: tuple = cursor.fetchall()[0]

    operation_type: str = data[0]
    category: str = data[1]
    value: float = data[2]

    if operation_type == 'income':
        # Load income from database
        income: dict = load_categories(user_id, operation_type='income')

        # Update data
        income[category]['value'] -= value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET income = %s, balance = balance - %s WHERE user_id = %s', (json.dumps(income, ensure_ascii=False), value, user_id))
        connection.commit()
    elif operation_type == 'expense':
        # Load income from database
        expense: dict = load_categories(user_id, operation_type='expense')

        # Update data
        expense[category]['value'] -= value

        # Update income data in database/users.
        cursor.execute('UPDATE users SET expense = %s, balance = balance + %s WHERE user_id = %s', (json.dumps(expense, ensure_ascii=False), value, user_id))
        connection.commit()

    # Delete operation from database/operations.
    cursor.execute('DELETE FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1', (user_id, ))
    connection.commit()