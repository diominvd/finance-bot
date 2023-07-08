from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database.load
import lines
import storage
from keyboards.inline.categories_keyboard import create_categories_keyboard
from states import AddExpense
import utils as u


router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu-keyboard']['expense']))
async def expense_command_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)

    # Check categories list.
    categories: dict = database.load.load_categories(user_id, 'expense')
    if len(categories) == 0:
        await message.answer(text=lines.new_operation_lines['e-t-categories-empty'])
    else:
        # Remove menu keyboard from dialog.
        await u.remove_reply_keyboard(message)

        # Create operation in bot storage.
        storage.create_operation(user_id, 'expense')

        # Load expense categories for create categories keyboard.
        expense_categories: dict = database.load.load_categories(user_id, 'expense')

        # Send message with categories.
        await message.answer(text=lines.new_operation_lines['t-choose-category'],
                             reply_markup=create_categories_keyboard(expense_categories))

        # Set state AddExpense.set_expense_category.
        await state.set_state(AddExpense.set_expense_category)