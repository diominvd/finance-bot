from config import BOT_STORAGE
import handlers
import pydantic.main


def insert_operation_into_bot_storage(obj: pydantic.main.ModelMetaclass) -> None:
    user_id: int = handlers.fetch_user_id(obj=obj)

    try:
        BOT_STORAGE[user_id] = {
            'category': str,
            'value': float,
            'date': str
        }
    except:
        print(f'> storage -> {user_id} -> new_operation: error.')
    else:
        print(f'> storage -> {user_id} -> new_operation: success.')


def update_operation_data_in_bot_storage(obj: pydantic.main.ModelMetaclass, field: str, value) -> None:
    user_id: int = handlers.fetch_user_id(obj=obj)

    try:
        BOT_STORAGE[user_id][field] = value
    except:
        print(f'> storage -> {user_id} -> update operation field={field}, value={value}: error.')
    else:
        print(f'> storage -> {user_id} -> update operation field={field}, value={value}: success.')