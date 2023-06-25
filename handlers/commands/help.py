from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import menu_kb
from strings import commands

router = Router(name=__name__)

@router.message(Command('help'))
async def start_command_handler(message: Message) -> None:
    await message.answer(text=commands['help_command_text'],
                         reply_markup=menu_kb)