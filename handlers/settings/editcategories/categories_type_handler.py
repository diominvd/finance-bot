from aiogram import Router, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import lines
from keyboards import EditCategoriesModeKeyboard
from states import EditCategories, EditIncomeCategories, EditExpenseCategories

router = Router(name=__name__)


@router.message(EditCategories.choose_categories_type, Text([lines.keyboards_lines['categories-type-keyboard']['income'], lines.keyboards_lines['categories-type-keyboard']['expense']]))
async def categories_type_handler(message: Message, state: FSMContext) -> None:
    # Send message with edit mode keyboard (add or delete buttons).
    await message.answer(text=lines.edit_categories_lines['t-choose-edit-mode'],
                         reply_markup=EditCategoriesModeKeyboard)

    # Check type of categories.
    match message.text:
        case '📈 | Категории доходов':
            await state.set_state(EditIncomeCategories.get_mode)
        case '📉 | Категории расходов':
            await state.set_state(EditExpenseCategories.get_mode)
