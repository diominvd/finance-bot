from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from data.database import database_functions
import handlers
from keyboards import menu_kb
from strings import commands


router = Router(name=__name__)


@router.message(Command('start'))
async def start_command_handler(message: Message) -> None:
    # Insert user into database.
    database_functions.insert_new_user_into_database(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=commands['start_command_text'],
                         reply_markup=menu_kb)