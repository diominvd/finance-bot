from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database.load
import lines
import storage
from keyboards.inline.categories_keyboard import create_categories_keyboard
from states import AddIncome
import utils as u


router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu-keyboard']['income']))
async def income_command_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)

    # Remove menu keyboard from dialog.
    await u.remove_reply_keyboard(message)

    # Create operation in bot storage.
    storage.create_operation(user_id, 'income')

    # Load expense categories for create categories keyboard.
    income_categories: dict = database.load.load_categories(user_id, 'income')

    # Send message with categories.
    await message.answer(text=lines.new_operation_lines['t-choose-category'],
                         reply_markup=create_categories_keyboard(income_categories))

    # Set state AddIncome.set_income_category.
    await state.set_state(AddIncome.set_income_category)