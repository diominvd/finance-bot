from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import config
from data import database
import handlers
from keyboards import menu_kb
from lines import currency_lines, commands_lines
from states import ChooseCurrencyStates

router = Router(name=__name__)


@router.callback_query(ChooseCurrencyStates.get_currency, Text(startswith='currency_'))
async def currency_handler(callback_query: CallbackQuery, state: FSMContext, bot=config.bot):
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Fetch currency from callback.
    user_currency: str = callback_query.data.split('_')[1]

    # Create user in database.
    database.insert_new_user_into_database_users(user_id=handlers.fetch_user_id(obj=callback_query), currency=user_currency)
    chat_id = callback_query.message.chat.id

    await bot.delete_message(chat_id=chat_id,
                             message_id=callback_query.message.message_id)

    await bot.send_message(chat_id=chat_id,
                           text=currency_lines['def_text_currency_chosen'](symbol=user_currency))

    await bot.send_message(chat_id=chat_id,
                           text=commands_lines['text_start_command'],
                           reply_markup=menu_kb)

    # Clear all states.
    await state.clear()
