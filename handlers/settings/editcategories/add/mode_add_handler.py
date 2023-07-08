from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import lines
from keyboards import AddCategoriesKeyboard
from states import EditIncomeCategories, EditExpenseCategories
import utils as u


router = Router(name=__name__)


@router.message(EditIncomeCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['add']))
@router.message(EditExpenseCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['add']))
async def edit_delete_mode_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)

    # Set the appropriate state for add categories.
    match await state.get_state():
        case 'EditIncomeCategories:get_mode':
            # Set state -> EditIncomeCategories.get_categories_for_add.
            await state.set_state(EditIncomeCategories.get_categories_for_add)
        case 'EditExpenseCategories:get_mode':
            # Set state -> EditExpenseCategories.get_categories_for_add.
            await state.set_state(EditExpenseCategories.get_categories_for_add)

    # Sending a message with the appropriate keyboard.
    await message.answer(text=lines.edit_categories_lines['t-categories-for-add'],
                         reply_markup=AddCategoriesKeyboard)
