from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import database
import emoji
import lines
import storage
import utils as u
from states import FirstStart


router = Router(name=__name__)


@router.callback_query(FirstStart.set_currency, Text(startswith='currency_'))
async def currency_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    # Fetch user currency from callback.
    user_id: int = u.fetch_user_id(callback)
    currency: str = callback.data.split('_')[1]

    # Add currency in bot storage.
    storage.update_storage_data(user_id=u.fetch_user_id(callback), key='currency', value=currency)

    await bot.edit_message_reply_markup(chat_id=u.fetch_chat_id(callback),
                                        message_id=u.fetch_message_id(callback),
                                        reply_markup=None)

    await bot.send_message(chat_id=u.fetch_chat_id(callback),
                           text=lines.first_start_lines['text_set_balance'])

    await state.set_state(FirstStart.set_balance)


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


@router.message(FirstStart.set_income_categories)
async def income_categories_handler(message: Message, state: FSMContext) -> None:
    income_categories_list: list = message.text.split('\n')
    income_categories: dict = {}

    try:
        # Formatted income categories.
        for category in income_categories_list:
            new_category = category.split(' ')
            income_categories[new_category[0].title()] = {
                'title': new_category[0].title(),
                'emoji': emoji.demojize(new_category[1]),
                'value': 0
            }
    except:
        await message.answer(text=lines.first_start_lines['error_text_incorrect_categories'])
    else:
        # Add income categories to bot storage.
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='income', value=income_categories)

        await message.answer(text=lines.first_start_lines['text_set_expense_categories'])

        await state.set_state(FirstStart.set_expense_categories)


@router.message(FirstStart.set_expense_categories)
async def expense_categories_handler(message: Message, state: FSMContext) -> None:
    expense_categories_list: list = message.text.split('\n')
    expense_categories: dict = {}

    try:
        # Formatted income categories.
        for category in expense_categories_list:
            new_category = category.split(' ')
            expense_categories[new_category[0].title()] = {
                'title': new_category[0].title(),
                'emoji': emoji.demojize(new_category[1]),
                'value': 0
            }
    except:
        await message.answer(text=lines.first_start_lines['error_text_incorrect_categories'])
    else:
        # Add income categories to bot storage.
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='expense', value=expense_categories)

        await message.answer(text=lines.first_start_lines['text_first_start_complete'])
        await message.answer(text=lines.commands_lines['command_text_start'])

        # Create new user in database.
        database.create_user(user_id=u.fetch_user_id(message))

        await state.clear()