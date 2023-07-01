from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from lines import commands_lines

router = Router(name=__name__)

@router.message(Command('help'))
async def start_command_handler(message: Message) -> None:
    await message.answer(text=commands_lines['text_help_command'])