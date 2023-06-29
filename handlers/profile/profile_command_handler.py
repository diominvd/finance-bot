from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text

import handlers
from keyboards import menu_kb
import lines

router = Router(name=__name__)

@router.message(Text('Профиль'))
async def profile_command_handler(message: Message) -> None:
    # Generate message with all user statistic.
    message_text: str = lines.profile_lines['def_text_statistic'](username=handlers.fetch_user_username(obj=message), user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=message_text,
                         reply_markup=menu_kb)