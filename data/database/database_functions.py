from config import bot_storage
from data import connection, cursor


def insert_new_user_into_database(user_id: int) -> None:
    try:
        cursor.execute(f'INSERT INTO users VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',
                       (user_id,))
    except:
        print(f'> insert user {user_id} into database/users: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/users: success.')


def insert_operation_into_database(user_id: int) -> None:
    # Fetch operation data from boot storage.
    category: str = bot_storage[user_id]['category']
    value: float = bot_storage[user_id]['value']
    date: str = bot_storage[user_id]['date']

    try:
        # Operation data -> database/operations.
        cursor.execute(f'INSERT INTO operations (user_id, category, value, date) VALUES (?, ?, ?, ?)',
                       (user_id, category, value, date))
        connection.commit()

        # Operation data -> database/users.
        cursor.execute(f'UPDATE users SET {category} = {category} + ?, total = total + ? WHERE user_id = ?',
                       (value, value, user_id))
        connection.commit()
    except:
        print(f'> storage -> {user_id} -> operation data -> database: error.')
    else:
        print(f'> storage -> {user_id} -> operation data -> database: success.')
