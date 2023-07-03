from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards import settings_kb
from lines import keyboards_lines, settings_lines
from states import SettingsStates


router = Router(name=__name__)
"""
    File Documentation:
        'func' in def names = function.
        'h' in def names = handler.
        'cb' in def names = callback.
"""


"1. Handler: get command and go to settings State."
@router.message(Text(keyboards_lines['menu_keyboard']['settings']))
async def func_settings_h(message: Message, state: FSMContext) -> None:
    await message.answer(text=settings_lines['text_settings'],
                         reply_markup=settings_kb)

    # Set state -> SettingsStates.get_mode.
    await state.set_state(SettingsStates.get_mode)