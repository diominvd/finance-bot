from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text

import utils as u
from keyboards import menu_kb
from lines import keyboards_lines, profile_lines


router = Router(name=__name__)
"""
    File Documentation:
        'func' in def names = function.
        'h' in def names = handler.
"""


"1. Handler: get command and output profile statistic."
@router.message(Text(keyboards_lines['menu_keyboard']['profile']))
async def func_profile_h(message: Message) -> None:
    # Generate message with all user statistic.
    message_text: str = profile_lines['def_text_statistic'](username=u.fetch_user_username(message), user_id=u.fetch_user_id(message))

    await message.answer(text=message_text,
                         reply_markup=menu_kb)