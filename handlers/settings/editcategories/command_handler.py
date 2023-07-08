from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database.load
import lines
from keyboards import CategoriesTypeKeyboard
from states import SettingsStates, EditCategories
import utils as u


router = Router(name=__name__)


@router.message(SettingsStates.get_mode, Text(lines.keyboards_lines['settings-keyboard']['edit-categories']))
async def command_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=lines.edit_categories_lines['t-choose-categories-type'],
                         reply_markup=CategoriesTypeKeyboard)

    # Set state EditCategories.choose_categories_type.
    await state.set_state(EditCategories.choose_categories_type)