from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import lines


router = Router(name=__name__)


@router.message(Command('info'))
async def command_start_handler(message: Message) -> None:
    await message.answer(text=lines.commands_lines['command_text_info'])