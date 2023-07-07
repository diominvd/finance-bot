from database import cursor, connection


def check_user(user_id: int):
    # Check user_id in database:users.
    cursor.execute('SELECT user_id FROM users WHERE user_id = %s', (user_id, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True