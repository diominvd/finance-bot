from config import bot_storage
from data import database


def create_operation(user_id: int) -> None:
    try:
        bot_storage[user_id] = {
            'currency': database.select_user_currency(user_id=user_id),
            'category': str,
            'value': float,
            'date': str
        }
    except:
        print(f'> storage -> {user_id} -> new_operation: error.')
    else:
        print(f'> storage -> {user_id} -> new_operation: success.')


def update_operation_data(user_id: int, field: str, value) -> None:
    try:
        bot_storage[user_id][field] = value
    except:
        print(f'> storage -> {user_id} -> update operation field={field}, value={value}: error.')
    else:
        print(f'> storage -> {user_id} -> update operation field={field}, value={value}: success.')


def remove_operation(user_id: int) -> None:
    bot_storage.pop(user_id, None)