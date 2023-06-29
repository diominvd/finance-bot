from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from data import database
import handlers
from keyboards import menu_kb
import lines

router = Router(name=__name__)

@router.message(Command('start'))
async def start_command_handler(message: Message) -> None:
    # Insert user into database.
    database.insert_new_user_into_database_users(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=lines.commands_lines['text_start_command'],
                         reply_markup=menu_kb)