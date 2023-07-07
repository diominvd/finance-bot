from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import lines
import storage
from states import FirstStart
import utils as u


router = Router(name=__name__)


@router.message(FirstStart.set_income_categories)
async def income_categories_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)

    try:
        # Try fetch categories from Message.
        income_categories: dict = u.generate_categories(message)
    except:
        # Send error message.
        await message.answer(text=lines.first_start_lines['e-t-incorrect-categories'])
    else:
        # Update user data (income categories) in bot storage.
        storage.update_storage_data(user_id, 'income', income_categories)

        # Send message for get expense categories.
        await message.answer(text=lines.first_start_lines['t-set-expense-categories'])

        # Set state FirstStart.set_expense_categories.
        await state.set_state(FirstStart.set_expense_categories)