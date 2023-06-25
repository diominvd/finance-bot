from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text

import handlers
import strings

router = Router(name=__name__)

@router.message(Text('Настройки'))
async def settings_command_handler(message: Message):
    await message.answer(text='Пока недоступно')