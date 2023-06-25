from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text

import handlers
from data.database import database_functions
from keyboards import menu_kb
import strings

router = Router(name=__name__)

@router.message(Text('Профиль'))
async def profile_command_handler(message: Message) -> None:
    # Fetch all operations and first operation date from database.
    all_operations = database_functions.select_all_operations_from_database(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=strings.profile['output_statistic'](username=handlers.fetch_user_username(obj=message),
                                                                  operations_list=all_operations,
                                                                  current_date=handlers.date_formation()),
                         reply_markup=menu_kb)