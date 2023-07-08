from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import lines
import storage
from states import FirstStart
import utils as u


router = Router(name=__name__)


@router.message(FirstStart.set_balance)
async def balance_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)
    user_currency: int = storage.bot_storage[user_id]['currency']

    try:
        # Try to transform message text to float value.
        balance: float = float(message.text)
    except:
        await message.answer(text=lines.first_start_lines['e-t-wrong-balance'])
    else:
        # Check sign of balance.
        if balance < 0:
            await message.answer(text=lines.first_start_lines['e-t-wrong-balance'])
        else:
            # Update user data (balance) in bot storage.
            storage.update_storage_data(user_id, 'balance', balance)

            # Send message with chosen balance.
            await bot.send_message(chat_id=chat_id,
                                   text=f"{lines.first_start_lines['t-balance-set']}{balance} {user_currency}")

            # Send message for get income categories.
            await message.answer(text=lines.first_start_lines['t-set-income-categories'])

            # Set state FirstStart.set_income_categories.
            await state.set_state(FirstStart.set_income_categories)