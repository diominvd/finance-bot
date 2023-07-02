from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from config import bot
from data import database
from handlers import utils as u

import keyboards
from keyboards import menu_kb, last_operations_kb
from keyboards.inline import currencies_keyboard

from lines import last_operations_lines

from states import LastOperationsStates


router = Router(name=__name__)
"""
    File Documentation:
        'func' in def names = function.
        'h' in def names = handler.
        'cb' in def names = callback.
"""


"1. Handler: handle command for look last operations."
@router.message(Text('Последние операции'))
async def func_last_operations_h(message: Message, state: FSMContext) -> None:
    # Checking that the user has operations.
    if database.operations_existence_check(user_id=u.fetch_user_id(message)):
        # Remove menu reply keyboard.
        await keyboards.delete_reply_keyboard(message)

        await message.answer(text=last_operations_lines['def_text_last_operations'](user_id=u.fetch_user_id(message)),
                             reply_markup=last_operations_kb)

        # Set state -> LastOperationsStates.get_callback.
        await state.set_state(LastOperationsStates.get_callback)
    else:
        await message.answer(text=last_operations_lines['error_text_last_operations_empty'],
                             reply_markup=menu_kb)


@u.remove_callback_delay
@router.callback_query(LastOperationsStates.get_callback, Text('delete_last'))
async def cb_last_operations_h(callback_query: CallbackQuery, state: FSMContext, bot=bot) -> None:
    # Checking that the user has operations.
    if database.operations_existence_check(database.select_operations(user_id=u.fetch_user_id(callback_query))):
        await bot.edit_message_text(text=last_operations_lines['def_text_last_operations'](user_id=u.fetch_user_id(callback_query)),
                                    chat_id=u.fetch_chat_id(callback_query),
                                    message_id=u.fetch_message_id(callback_query),
                                    reply_markup=last_operations_kb)
    else:
        # Delete message with last operations.
        await bot.delete_message(chat_id=u.fetch_chat_id(callback_query),
                                 message_id=u.fetch_message_id(callback_query))

        # Send message with menu keyboard.
        await bot.send_message(chat_id=u.fetch_chat_id(callback_query),
                               text=last_operations_lines['error_text_last_operations_empty'],
                               reply_markup=menu_kb)

        # Clear all states = Return to main menu.
        await state.clear()