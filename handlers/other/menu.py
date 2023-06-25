from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.filters import Text

import config
from keyboards import menu_kb
from strings import other


router = Router(name=__name__)


@router.callback_query(Text('menu'))
async def menu_callback_handler(callback_query: CallbackQuery, state: FSMContext, bot=config.bot):
    # Remove inline keyboard from message.
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=None)

    # Send loading message.
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=other['back_to_menu'],
                           reply_markup=menu_kb)

    # Clear all states.
    await state.clear()