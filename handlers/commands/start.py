from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import menu_kb
from strings import commands


router = Router(name=__name__)


@router.message(Command('start'))
async def start_command_handler(message: Message):
    await message.answer(text=commands['start_command_text'],
                         reply_markup=menu_kb)