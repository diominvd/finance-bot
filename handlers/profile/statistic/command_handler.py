from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

import database.load
import lines
from states import ProfileStates
import utils as u


router = Router(name=__name__)


@router.message(ProfileStates.get_mode, Text(lines.keyboards_lines['profile-keyboard']['statistic']))
async def statistic_command_handler(message: Message,) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)

    # Load income categories.
    income_categories: dict = database.load.load_categories(user_id, 'income')

    # Load expense categories.
    expense_categories: dict = database.load.load_categories(user_id, 'expense')

    # Load first date
    first_date: str = database.load.load_first_date(user_id)

    # Load user currency.
    user_currency: str = database.load.load_user_currency(user_id)

    # Send message with statistic.
    await message.answer(text=lines.profile_lines['d-t-load-statistic'](income_categories, expense_categories, user_currency, first_date))