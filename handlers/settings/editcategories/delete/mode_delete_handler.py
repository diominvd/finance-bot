from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database.load
import lines
from keyboards.inline import categories_for_delete_keyboard
from states import EditIncomeCategories, EditExpenseCategories
import utils as u


router = Router(name=__name__)


@router.message(EditIncomeCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['delete']))
@router.message(EditExpenseCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['delete']))
async def edit_delete_mode_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)

    # Loading the appropriate categories for the user.
    match await state.get_state():
        case 'EditIncomeCategories:get_mode':
            categories: dict = database.load.load_categories(user_id, 'income')

            # Set state -> EditIncomeCategories.get_categories_for_delete.
            await state.set_state(EditIncomeCategories.get_categories_for_delete)
        case 'EditExpenseCategories:get_mode':
            categories: dict = database.load.load_categories(user_id, 'expense')

            # Set state -> EditExpenseCategories.get_categories_for_delete.
            await state.set_state(EditExpenseCategories.get_categories_for_delete)

    # Delete reply markup.
    await u.remove_reply_keyboard(message)

    # Send message with categories for delete.
    await message.answer(text=lines.edit_categories_lines['t-categories-for-delete'],
                         reply_markup=categories_for_delete_keyboard.create_categories_for_delete_keyboard(categories))
