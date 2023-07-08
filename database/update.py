import json

import database.load
from database import connection, cursor
import storage


def create_user(user_id: int) -> None:
    user_id: int = storage.bot_storage[user_id]['user_id']
    username: str = storage.bot_storage[user_id]['username']
    currency: str = storage.bot_storage[user_id]['currency']
    balance: float = storage.bot_storage[user_id]['balance']
    income: dict = storage.bot_storage[user_id]['income']
    expense: dict = storage.bot_storage[user_id]['expense']

    cursor.execute('''INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s);''',
                   (user_id, username, currency, balance, json.dumps(income, ensure_ascii=False), json.dumps(expense, ensure_ascii=False)))
    connection.commit()


def add_operation(user_id: int) -> None:
    # Fetch operation data from bot storage.
    user_id: int = storage.bot_storage[user_id]['user_id']
    operation_type: str = storage.bot_storage[user_id]['operation_type']
    currency: str = storage.bot_storage[user_id]['currency']
    category: str = storage.bot_storage[user_id]['category']
    value: float = storage.bot_storage[user_id]['value']
    date: str = storage.bot_storage[user_id]['date']

    # Loading categories depending on the operation.
    categories: dict = database.load.load_categories(user_id, operation_type)

    # Update category value in categories dict.
    categories[category]['value'] += value

    match operation_type:
        case 'income':
            # Update income data.
            cursor.execute('UPDATE users SET income = %s, balance = balance + %s WHERE user_id = %s',
                           (json.dumps(categories, ensure_ascii=False), value, user_id))
        case 'expense':
            # Update expense data.
            cursor.execute('UPDATE users SET expense = %s, balance = balance - %s WHERE user_id = %s',
                           (json.dumps(categories, ensure_ascii=False), value, user_id))

    # Save changes into database/users.
    connection.commit()

    # Save operation into database/operations.
    cursor.execute('''INSERT INTO operations (user_id, operation_type, currency, category, value, date) VALUES (%s, %s, %s, %s, %s, %s);''',
                   (user_id, operation_type, currency, category, value, date))
    connection.commit()


def delete_last_operation(user_id: int) -> None:
    # Fetch last operation data.
    cursor.execute('SELECT operation_type, category, value FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1', (user_id, ))
    data: tuple = cursor.fetchall()[0]

    # Extract operation data from tuple.
    operation_type: str = data[0]
    category: str = data[1]
    value: float = data[2]

    # Loading categories depending on the operation.
    categories: dict = database.load.load_categories(user_id, operation_type)

    # If operation category was deleted from users categories just delete category from history and change balance.
    try:
        # Update category value in categories dict.
        categories[category]['value'] -= value
    except:
        # Delete operation from database/operations.
        cursor.execute('DELETE FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1', (user_id,))
        connection.commit()

        # Update balance.
        match operation_type:
            case 'income':
                cursor.execute('UPDATE users SET balance = balance - %s WHERE user_id = %s',
                               (value, user_id))
            case 'expense':
                cursor.execute('UPDATE users SET balance = balance + %s WHERE user_id = %s',
                               (value, user_id))
    else:
        match operation_type:
            case 'income':
                # Update income data.
                cursor.execute('UPDATE users SET income = %s, balance = balance - %s WHERE user_id = %s',
                               (json.dumps(categories, ensure_ascii=False), value, user_id))
            case 'expense':
                # Update expense data.
                cursor.execute('UPDATE users SET expense = %s, balance = balance + %s WHERE user_id = %s',
                               (json.dumps(categories, ensure_ascii=False), value, user_id))

        # Save changes into database/users.
        connection.commit()

        # Delete operation from database/operations.
        cursor.execute('DELETE FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1', (user_id, ))
        connection.commit()


def update_categories(user_id: int, category_type: str, categories: dict) -> None:
    match category_type:
        case 'income':
            cursor.execute('UPDATE users SET income = %s WHERE user_id = %s',
                           (json.dumps(categories, ensure_ascii=False), user_id))
        case 'expense':
            cursor.execute('UPDATE users SET expense = %s WHERE user_id = %s',
                           (json.dumps(categories, ensure_ascii=False), user_id))

    # Save changes in database.
    connection.commit()