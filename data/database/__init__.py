from config import bot_storage
from data import connection, cursor


def create_user(user_id: int, currency: str) -> None:
    try:
        cursor.execute(f'INSERT INTO users VALUES (%s, %s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',
                       (user_id, currency))
    except:
        print(f'> insert user {user_id} into database/users: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/users: success.')


def user_existence_check(user_id: int) -> bool:
    cursor.execute(f'SELECT user_id FROM users WHERE user_id = %s', (user_id, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


def add_operation(user_id: int) -> None:
    # Fetch operation data from boot storage.
    currency: str = bot_storage[user_id]['currency']
    category: str = bot_storage[user_id]['category']
    value: float = bot_storage[user_id]['value']
    date: str = bot_storage[user_id]['date']

    try:
        # Insert operation data into database/operations.
        cursor.execute(f'INSERT INTO operations (user_id, currency, category, value, date) VALUES (%s, %s, %s, %s, %s)',
                       (user_id, currency, category, value, date))
        connection.commit()
        print('operations good')

        # Update user data in database/users.
        cursor.execute(f'UPDATE users SET {category} = {category} + %s, total = total + %s WHERE user_id = %s',
                       (value, value, user_id))
        connection.commit()
    except:
        print(f'> storage -> {user_id} -> operation data -> database: error.')
    else:
        print(f'> storage -> {user_id} -> operation data -> database: success.')


def select_operations(user_id: int, limit: int = 999999) -> list:
    # Fetch all operations from database/operations.
    cursor.execute(f'SELECT currency, category, value, date FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT %s',
                   (user_id, limit))

    # Last operations: list with tuples like [(operation_data), (operation_data), ...]
    operations_list: list = list(reversed(cursor.fetchall()))

    return operations_list


def operations_existence_check(user_id: int) -> bool:
    if len(select_operations(user_id)) == 0:
        return False
    else:
        return True


def select_user_currency(user_id: int) -> str:
    cursor.execute(f'SELECT currency FROM users WHERE user_id = %s', (user_id, ))
    return cursor.fetchall()[0][0]


def update_user_currency(user_id: int, currency: str) -> None:
    cursor.execute(f'UPDATE users SET currency = %s WHERE user_id = %s', (currency, user_id))
    connection.commit()


def delete_last_operation(user_id: int) -> list:
    # Fetch operation category and value for update database/users.
    cursor.execute(f'SELECT category, value FROM operations WHERE user_id =%s ORDER BY operation_id DESC LIMIT 1',
                   (user_id,))
    operation_data: tuple = cursor.fetchall()[0]

    # Fetch category and value from operation_data.
    category: str = operation_data[0]
    value: float = operation_data[1]

    # Delete operation value from database/users.
    cursor.execute(f'UPDATE users SET {category} = {category} - %s, total = total - %s WHERE user_id = %s',
                   (value, value, user_id))
    connection.commit()

    # Delete operation from database/operations.
    cursor.execute(f'DELETE FROM operations WHERE user_id = %s ORDER BY operation_id DESC LIMIT 1',
                   (user_id,))
    connection.commit()

    # Last operations: list with refreshed operations list.
    last_operations: list = select_operations(user_id=user_id, limit=5)

    return last_operations


def delete_all_operations(user_id: int) -> None:
    # Delete all operations from database/operations.
    cursor.execute(f'DELETE FROM operations WHERE user_id = %s', (user_id, ))
    connection.commit()

    # Set default values = 0 in database/users.
    cursor.execute(f'UPDATE users SET products = 0, cafes = 0, auto = 0, transport = 0, home = 0, entertainment = 0, '
                   f'sport = 0, health = 0, education = 0, gifts = 0, beauty = 0, clothes = 0, technic = 0, subscriptions = 0, total = 0 '
                   f'WHERE user_id = %s', (user_id, ))
    connection.commit()