import pydantic.main
from aiogram import Router
from aiogram.fsm.context import FSMContext
import aiogram.types
from aiogram.filters import Text

import config
from handlers import utils as u
from keyboards import menu_kb
import lines
from lines import keyboards_lines


router = Router(name=__name__)
"""
    File Documentation:
        'func' in def names = function.
        'h' in def names = handler.
        'cb' in def names = callback.
"""


"1. Handler: back to main menu."
@router.message(Text(keyboards_lines['settings_keyboard']['menu']))
async def func_menu_cb_h(obj: pydantic.main.ModelMetaclass, state: FSMContext, bot=config.bot) -> None:
    match type(obj):
        case aiogram.types.Message:
            # Send loading message.
            await bot.send_message(chat_id=u.fetch_chat_id(obj),
                                   text=lines.other_lines['text_back_menu'],
                                   reply_markup=menu_kb)

    # Clear all states.
    await state.clear()


@router.callback_query(Text('menu'))
@u.remove_callback_delay
async def func_menu_cb_h(obj: pydantic.main.ModelMetaclass, state: FSMContext, bot=config.bot) -> None:
    match type(obj):
        case aiogram.types.CallbackQuery:
            # Remove inline keyboard from message.
            await bot.edit_message_reply_markup(chat_id=u.fetch_chat_id(obj),
                                                message_id=u.fetch_message_id(obj),
                                                reply_markup=None)

            # Send loading message.
            await bot.send_message(chat_id=u.fetch_chat_id(obj),
                                   text=lines.other_lines['text_back_menu'],
                                   reply_markup=menu_kb)

    # Clear all states.
    await state.clear()