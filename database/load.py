import json

from database import connection, cursor
import storage


def load_categories(user_id: int, category_type: str) -> dict:
    match category_type:
        case 'income':
            cursor.execute('SELECT income FROM users WHERE user_id = %s', (user_id, ))
            categories: dict = json.loads(str(cursor.fetchall()[0][0]))

            return categories
        case 'expense':
            cursor.execute('SELECT expense FROM users WHERE user_id = %s', (user_id,))
            categories: dict = json.loads(str(cursor.fetchall()[0][0]))

            return categories


def load_profile_info(user_id: int) -> tuple:
    cursor.execute('SELECT username, currency, balance FROM users WHERE user_id = %s', (user_id, ))
    return cursor.fetchall()[0]


def load_last_operations(user_id: int) -> list:
    cursor.execute('SELECT operation_type, currency, category, value, date FROM operations WHERE user_id = %s LIMIT 10', (user_id, ))
    return cursor.fetchall()


def load_user_currency(user_id: int) -> str:
    cursor.execute('''SELECT currency FROM users WHERE user_id = %s''', (user_id, ))
    return cursor.fetchall()[0][0]