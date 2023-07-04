import aiogram
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State
import config
from pydantic.main import ModelMetaclass


def fetch_user_id(obj: ModelMetaclass) -> int:
    return int(obj.from_user.id)


def fetch_chat_id(obj: ModelMetaclass) -> int:
    match type(obj):
        case aiogram.types.Message:
            return int(obj.chat.id)
        case aiogram.types.CallbackQuery:
            return int(obj.message.chat.id)


def fetch_message_id(obj: ModelMetaclass) -> int:
    match type(obj):
        case aiogram.types.Message:
            return int(obj.message_id)
        case aiogram.types.CallbackQuery:
            return int(obj.message.message_id)

def fetch_user_username(obj: ModelMetaclass) -> str:
    return str(obj.from_user.username)


def remove_callback_delay(func):
    async def wrapper(obj: ModelMetaclass, state: State):
        await obj.answer()
        return await func(obj, state)
    return wrapper


async def remove_reply_keyboard(message: Message, bot=config.bot) -> None:
    await message.answer(text='Загрузка...',
                         reply_markup=ReplyKeyboardRemove())

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)