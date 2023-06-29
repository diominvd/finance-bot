from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import menu_kb
from lines import commands_lines

router = Router(name=__name__)

@router.message(Command('help'))
async def start_command_handler(message: Message) -> None:
    await message.answer(text=commands_lines['text_help_command'],
                         reply_markup=menu_kb)