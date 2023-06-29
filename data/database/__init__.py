from config import bot_storage
from data import connection, cursor


def insert_new_user_into_database_users(user_id: int) -> None:
    try:
        cursor.execute(f'INSERT INTO users VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',
                       (user_id,))
    except:
        print(f'> insert user {user_id} into database/users: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/users: success.')


def insert_operation_into_database_operations(user_id: int) -> None:
    # Fetch operation data from boot storage.
    category: str = bot_storage[user_id]['category']
    value: float = bot_storage[user_id]['value']
    date: str = bot_storage[user_id]['date']

    try:
        # Insert operation data into database/operations.
        cursor.execute(f'INSERT INTO operations (user_id, category, value, date) VALUES (?, ?, ?, ?)',
                       (user_id, category, value, date))
        connection.commit()

        # Update user data in database/users.
        cursor.execute(f'UPDATE users SET {category} = {category} + ?, total = total + ? WHERE user_id = ?',
                       (value, value, user_id))
        connection.commit()
    except:
        print(f'> storage -> {user_id} -> operation data -> database: error.')
    else:
        print(f'> storage -> {user_id} -> operation data -> database: success.')


def select_operations_from_database_operations(user_id: int, limit: int = 999999) -> list:
    # Fetch all operations from database/operations.
    cursor.execute(f'SELECT category, value, date FROM operations WHERE user_id = ? ORDER BY operation_id DESC LIMIT ?',
                   (user_id, limit))

    # Last operations: list with tuples like [(operation_data), (operation_data), ...]
    operations_list: list = list(reversed(cursor.fetchall()))

    return operations_list


def delete_last_operation_from_database(user_id: int) -> list:
    # Fetch operation category and value for update database/users.
    cursor.execute(f'SELECT category, value FROM operations WHERE user_id =? ORDER BY operation_id DESC LIMIT 1',
                   (user_id,))
    operation_data: tuple = cursor.fetchall()[0]

    # Fetch category and value from operation_data.
    category: str = operation_data[0]
    value: float = operation_data[1]

    # Delete operation value from database/users.
    cursor.execute(f'UPDATE users SET {category} = {category} - ?, total = total - ? WHERE user_id = ?',
                   (value, value, user_id))
    connection.commit()

    # Delete operation from database/operations.
    cursor.execute(f'DELETE FROM operations WHERE operation_id = (SELECT MAX(operation_id) FROM operations) and user_id = ?',
                   (user_id,))
    connection.commit()

    # Last operations: list with refreshed operations list.
    last_operations: list = select_operations_from_database_operations(user_id=user_id, limit=5)

    return last_operations


def delete_all_user_operations_from_database(user_id: int) -> None:
    # Delete all operations from database/operations.
    cursor.execute(f'DELETE FROM operations WHERE user_id = ?', (user_id, ))
    connection.commit()

    # Set default values = 0 in database/users.
    cursor.execute(f'UPDATE users SET products = 0, cafes = 0, auto = 0, transport = 0, home = 0, entertainment = 0, '
                   f'sport = 0, health = 0, education = 0, gifts = 0, beauty = 0, clothes = 0, technic = 0, subscriptions = 0, total = 0 '
                   f'WHERE user_id = ?', (user_id, ))
    connection.commit()