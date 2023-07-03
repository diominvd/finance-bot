from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data import database
import utils as u
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


"1. Handler: get command for clear all operations."
@router.message(SettingsStates.get_mode, Text(keyboards_lines['settings_keyboard']['clear_all_operations']))
async def delete_all_operations_handler(message: Message, state: FSMContext):
    # # Checking that the user has operations.
    if database.select_operations(user_id=u.fetch_user_id(message)):
        # Delete all operations from database.
        database.delete_all_operations(user_id=u.fetch_user_id(message))

        await message.answer(text=settings_lines['text_all_operations_deleted'],
                             reply_markup=settings_kb)
    else:
        await message.answer(text=settings_lines['error_text_operations_list_empty'],
                             reply_markup=settings_kb)

    # Clear all states.
    await state.clear()