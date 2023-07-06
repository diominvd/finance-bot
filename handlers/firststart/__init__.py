from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import database
from keyboards import menu_kb
import lines
from states import FirstStart
import storage
from storage import bot_storage
import utils as u


router = Router(name=__name__)

"Handler: fetch currency from callback and add it in bot storage."
@router.callback_query(FirstStart.set_currency, Text(startswith='currency_'))
async def currency_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    # Fetch user currency from callback.
    user_id: int = u.fetch_user_id(callback)
    currency: str = lines.keyboards_lines['currencies_keyboard'][callback.data.split('_')[1]]['text']

    # Add currency in bot storage.
    storage.update_storage_data(user_id=u.fetch_user_id(callback), key='currency', value=currency)

    await bot.edit_message_reply_markup(chat_id=u.fetch_chat_id(callback),
                                        message_id=u.fetch_message_id(callback),
                                        reply_markup=None)

    await bot.send_message(chat_id=u.fetch_chat_id(callback),
                           text=lines.first_start_lines['text_set_balance'])

    await state.set_state(FirstStart.set_balance)


"Handler: fetch balance and add it in bot storage."
@router.message(FirstStart.set_balance)
async def balance_handler(message: Message, state: FSMContext) -> None:
    try:
        balance: float = float(message.text)
    except:
        await message.answer(text=lines.first_start_lines['error_text_wrong_balance'])
    else:
        if balance < 0:
            await message.answer(text=lines.first_start_lines['error_text_wrong_balance'])
        else:
            # Add balance to bot storage.
            storage.update_storage_data(user_id=u.fetch_user_id(message), key='balance', value=balance)

            await message.answer(text=lines.first_start_lines['text_set_income_categories'])

            await state.set_state(FirstStart.set_income_categories)


"Handler: fetch income categories and add it in bot storage."
@router.message(FirstStart.set_income_categories)
async def income_categories_handler(message: Message, state: FSMContext) -> None:
    try:
        income_categories: dict = u.generate_categories(message)
    except:
        await message.answer(text=lines.first_start_lines['error_text_incorrect_categories'])
    else:
        # Add income categories to bot storage.
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='income', value=income_categories)

        await message.answer(text=lines.first_start_lines['text_set_expense_categories'])

        await state.set_state(FirstStart.set_expense_categories)


"Handler: fetch expense categories, add it in bot storage and synchronize with database."
@router.message(FirstStart.set_expense_categories)
async def expense_categories_handler(message: Message, state: FSMContext) -> None:
    try:
        expense_categories: dict = u.generate_categories(message)
    except:
        await message.answer(text=lines.first_start_lines['error_text_incorrect_categories'])
    else:
        # Add income categories to bot storage.
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='expense', value=expense_categories)

        await message.answer(text=lines.first_start_lines['text_first_start_complete'])
        await message.answer(text=lines.commands_lines['command_text_start'],
                             reply_markup=menu_kb)

        # Create new user in database.
        database.create_user(user_id=u.fetch_user_id(message))

        # Remove user from bot storage.
        user_id: int = u.fetch_user_id(message)
        bot_storage.pop(user_id, None)

        await state.clear()