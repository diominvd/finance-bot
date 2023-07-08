from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database.load
import database.update
import lines
from states import EditIncomeCategories, EditExpenseCategories
import utils as u


router = Router(name=__name__)


@router.message(EditIncomeCategories.get_categories_for_add)
@router.message(EditExpenseCategories.get_categories_for_add)
async def edit_new_categories_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)

    # Initializing categories dict.
    categories: dict = {}

    # Loading the appropriate categories for the user.
    match await state.get_state():
        case 'EditIncomeCategories:get_categories_for_add':
            categories: dict = database.load.load_categories(user_id, 'income')
        case 'EditExpenseCategories:get_categories_for_add':
            categories: dict = database.load.load_categories(user_id, 'expense')

    try:
        refreshed_categories: dict = u.add_category(message, categories)
    except:
        await message.answer(text=lines.edit_categories_lines['e-t-incorrect-category'])
    else:
        # Update categories in database.
        match await state.get_state():
            case 'EditIncomeCategories:get_categories_for_add':
                database.update.update_categories(user_id, 'income', refreshed_categories)
            case 'EditExpenseCategories:get_categories_for_add':
                database.update.update_categories(user_id, 'expense', refreshed_categories)

        await message.answer(text=lines.edit_categories_lines['t-category-added'])