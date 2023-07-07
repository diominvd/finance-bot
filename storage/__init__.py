import datetime
from pydantic.main import ModelMetaclass

import database.load
import utils as u


# Bot storage is necessary to monitor active operations that are in the process of being created.
bot_storage: dict = {}


def registration(message: ModelMetaclass) -> None:
    user_id: int = u.fetch_user_id(message)
    username: str = u.fetch_user_username(message)

    bot_storage[user_id]: dict = {}
    update_storage_data(user_id, 'user_id', user_id)
    update_storage_data(user_id, 'username', username)


def update_storage_data(user_id: int, key: str, value) -> None:
    bot_storage[user_id][key] = value


def create_operation(user_id: int, operation_type: str) -> None:
    # Formatted operation date.
    operation_date: list = list(reversed(str(datetime.date.today()).split('-')))
    operation_date: str = '.'.join(operation_date)
    operation_currency: str = database.load.load_user_currency(user_id)

    # Add operation
    bot_storage[user_id] = {
        'user_id': user_id,
        'operation_type': operation_type,
        'currency': operation_currency,
        'category': None,
        'emoji': None,
        'value': None,
        'date': operation_date
    }


def delete_operation(user_id: int) -> None:
    bot_storage.pop(user_id, None)
