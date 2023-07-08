import emoji
from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import config
import database.load
import lines
import storage
from states import AddExpense
import utils as u


router = Router(name=__name__)


@router.callback_query(AddExpense.set_expense_category, Text(startswith='category_'))
@u.remove_callback_delay
async def expense_category_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(callback)
    chat_id: int = u.fetch_chat_id(callback)

    # Load expense categories for fetch data.
    expense_categories: dict = database.load.load_categories(user_id, 'expense')

    # Fetch operation category from callback.
    operation_category: str = callback.data.split('_')[1]
    operation_category_emoji: str = emoji.emojize(expense_categories[operation_category]['emoji'])

    # Update operation data in bot storage.
    storage.update_storage_data(user_id, 'category', operation_category)
    storage.update_storage_data(user_id, 'emoji', operation_category_emoji)

    # Send message for get value of operation.
    await bot.edit_message_text(text=lines.new_operation_lines['d-t-category-set'](operation_category, operation_category_emoji),
                                chat_id=chat_id,
                                message_id=u.fetch_message_id(callback),
                                reply_markup=None)

    # Send message for get operation value.
    await bot.send_message(chat_id=user_id,
                           text=lines.new_operation_lines['t-choose-value'])

    # Set state AddExpense.set_expense_value.
    await state.set_state(AddExpense.set_expense_value)