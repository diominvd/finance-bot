from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import kb_menu
from lines.commands import commands


router = Router(name=__name__)


@router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(text=commands['start'],
                         reply_markup=kb_menu)