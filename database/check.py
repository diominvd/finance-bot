from database import cursor, connection
import database


@database.db_connect
def check_user(user_id: int):
    # Check user_id in database:users.
    cursor.execute('SELECT user_id FROM users WHERE user_id = %s', (user_id, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True

@database.db_connect
def check_user_balance(user_id: int, value: float) -> bool:
    cursor.execute('SELECT balance FROM users WHERE user_id = %s',
                   (user_id, ))
    balance: float = float(cursor.fetchall()[0][0])

    if balance - value < 0:
        return False
    else:
        return True