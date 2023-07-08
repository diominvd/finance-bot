from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database.update
import lines
import storage
from keyboards import MenuKeyboard
from states import FirstStart
import utils as u


router = Router(name=__name__)


@router.message(FirstStart.set_expense_categories)
async def expense_categories_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)

    try:
        # Try fetch categories from Message.
        expense_categories: dict = u.generate_categories(message)
    except:
        # Send error message.
        await message.answer(text=lines.first_start_lines['e-t-incorrect-categories'])
    else:
        # Update user data (income categories) in bot storage.
        storage.update_storage_data(user_id, 'expense', expense_categories)

        # Create new user in database.
        database.update.create_user(user_id)

        # Remove user from bot storage.
        storage.delete_operation(user_id)

        # Send message about Initial setup complete.
        await message.answer(text=lines.first_start_lines['t-initial-setup-complete'])

        # Send /start message with menu keyboard.
        await message.answer(text=lines.commands_lines['c-t-start'],
                             reply_markup=MenuKeyboard)

        # Clear all states -> Main Menu.
        await state.clear()