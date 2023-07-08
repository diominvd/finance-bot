from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import config
import lines
import storage
from states import FirstStart
import utils as u


router = Router(name=__name__)


@router.callback_query(FirstStart.set_currency, Text(startswith='currency_'))
@u.remove_callback_delay
async def currency_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(callback)
    chat_id: int = u.fetch_chat_id(callback)

    # Fetch user currency from callback.
    user_currency: str = lines.currencies[callback.data.split('_')[1]]['symbol']

    # Update user data (currency) in bot storage.
    storage.update_storage_data(user_id=u.fetch_user_id(callback), key='currency', value=user_currency)

    # Remove cure
    await bot.edit_message_text(text=f"{lines.first_start_lines['t-currency-set']}{callback.data.split('_')[1]}",
                                chat_id=chat_id,
                                message_id=u.fetch_message_id(callback),
                                reply_markup=None)

    # Sending a message to the user to set the current balance.
    await bot.send_message(chat_id=chat_id,
                           text=lines.first_start_lines['t-choose-balance'])

    # Set state FirstStart.set_balance.
    await state.set_state(FirstStart.set_balance)