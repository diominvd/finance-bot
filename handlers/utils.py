import aiogram
import pydantic.main


def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)


def fetch_chat_id(obj: pydantic.main.ModelMetaclass) -> int:
    match type(obj):
        case aiogram.types.Message:
            return int(obj.chat.id)
        case aiogram.types.CallbackQuery:
            return int(obj.message.chat.id)


def fetch_message_id(obj: pydantic.main.ModelMetaclass) -> int:
    match type(obj):
        case aiogram.types.Message:
            return int(obj.message_id)
        case aiogram.types.CallbackQuery:
            return int(obj.message.message_id)

def fetch_user_username(obj: pydantic.main.ModelMetaclass) -> str:
    return str(obj.from_user.username)


def remove_callback_delay(funct) -> None:
    async def wrapper(callback_query):
        await callback_query.answer(text=None,
                                    show_alert=None)
        funct(callback_query)
    return wrapper