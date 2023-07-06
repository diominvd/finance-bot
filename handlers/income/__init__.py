from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import database
import emoji
from keyboards.inline.categories_keyboard import create_categories_keyboard
from keyboards import menu_kb
import lines
from states import AddIncome
import storage
import utils as u

router = Router(name=__name__)

"Handler: fetch command to add income and send income categories."


@router.message(Text(lines.keyboards_lines['menu_keyboard']['income']))
async def operation_type_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    # Remove menu keyboard
    await u.remove_reply_keyboard(message, bot)

    # Create operation in bot storage.
    storage.create_operation_in_storage(user_id=u.fetch_user_id(message), operation_type='income', currency=database.fetch_user_currency(u.fetch_user_id(message)))

    income_categories: dict = database.load_categories(user_id=u.fetch_user_id(message), operation_type='income')

    await message.answer(text=lines.new_operation_lines['text_choose_income_category'],
                         reply_markup=create_categories_keyboard(categories=income_categories))

    await state.set_state(AddIncome.set_income_category)


"Handler: fetch category from callback and add it in bot storage."


@router.callback_query(AddIncome.set_income_category, Text(startswith='category_'))
@u.remove_callback_delay
async def income_category_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    # Fetch user income categories from database.
    income_categories: dict = database.load_categories(user_id=u.fetch_user_id(callback), operation_type='income')

    # Fetch operation category from callback.
    operation_category: str = callback.data.split('_')[1]

    # Update operation data in bot storage.
    user_id: int = u.fetch_user_id(callback)
    storage.update_storage_data(user_id, key='category', value=operation_category)
    storage.update_storage_data(user_id, key='emoji', value=emoji.emojize(income_categories[operation_category]['emoji']))

    await bot.edit_message_text(text=lines.new_operation_lines['def_text_category_set'](user_id),
                                chat_id=u.fetch_chat_id(callback),
                                message_id=u.fetch_message_id(callback),
                                reply_markup=None)

    await bot.send_message(chat_id=u.fetch_chat_id(callback),
                           text=lines.new_operation_lines['text_choose_operation_value'])

    await state.set_state(AddIncome.set_income_value)


"Handler: fetch operation value and save operation in database."


@router.message(AddIncome.set_income_value)
async def income_value_handler(message: Message, state: FSMContext, bot=config.bot):
    user_id: int = u.fetch_user_id(message)
    try:
        operation_value: float = float(message.text)
    except ValueError:
        await message.answer(text=lines.new_operation_lines['error_text_incorrect_value'])
    else:
        if operation_value < 0:
            await message.answer(text=lines.new_operation_lines['error_text_incorrect_value'])
        else:
            # Update operation data in storage.
            storage.update_storage_data(user_id, key='value', value=operation_value)

            # Add operation in db
            database.add_operation(user_id, operation_type='income')

            # Edit message with value query,
            await bot.edit_message_text(text=lines.new_operation_lines['def_text_value_set'](user_id),
                                        chat_id=u.fetch_chat_id(message),
                                        message_id=u.fetch_message_id(message) - 1)

            # Delete message with value from user.
            await bot.delete_message(chat_id=u.fetch_chat_id(message),
                                     message_id=u.fetch_message_id(message))

            await message.answer(text=lines.new_operation_lines['def_text_operation_complete'](user_id),
                                 reply_markup=menu_kb)

            # Remove operation from bot storage.
            storage.delete_operation_from_storage(user_id)

            # Return to menu.
            await state.clear()
