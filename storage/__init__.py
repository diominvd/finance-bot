import datetime

from pydantic.main import ModelMetaclass

import utils as u


# Bot storage is necessary to monitor active operations that are in the process of being created.
bot_storage: dict = {}


def update_storage_data(user_id: int, key: str, value) -> None:
    bot_storage[user_id][key] = value


def create_operation_in_storage(user_id: int, operation_type: str, currency: str) -> None:
    operation_date: list = list(reversed(str(datetime.date.today()).split('-')))
    operation_date: str = '.'.join(operation_date)
    bot_storage[user_id] = {
        'user_id': user_id,
        'operation_type': operation_type,
        'currency': currency,
        'category': None,
        'emoji': None,
        'value': None,
        'date': operation_date
    }


def delete_operation_from_storage(user_id: int) -> None:
    bot_storage.pop(user_id, None)
