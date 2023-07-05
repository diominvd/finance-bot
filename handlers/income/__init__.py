from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import database
import emoji
from keyboards.inline.categories_keyboard import create_categories_keyboard
import lines
import storage
import utils as u
from states import AddIncome


router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu_keyboard']['income']))
async def currency_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    # Remove menu keyboard
    await u.remove_reply_keyboard(message, bot)

    income_categories: dict = database.fetch_income_categories(user_id=u.fetch_user_id(message))

    await message.answer(text=lines.income_lines['text_choose_income_category'],
                         reply_markup=create_categories_keyboard(categories=income_categories))

    await state.set_state(AddIncome.set_income_category)