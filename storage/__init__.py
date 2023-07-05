from pydantic.main import ModelMetaclass

import utils as u


# Bot storage is necessary to monitor active operations that are in the process of being created.
bot_storage: dict = {}


def update_storage_data(user_id: int, key: str, value):
    bot_storage[user_id][key] = value
