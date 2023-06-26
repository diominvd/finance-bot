from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import config
import handlers
from data.database import database_functions
from keyboards import settings_kb
from states import SettingsStates
import strings

router = Router(name=__name__)

@router.message(SettingsStates.get_option, Text('Очистить список операций'))
async def settings_command_handler(message: Message):
    # Delete all operations from database.
    database_functions.delete_all_user_operations_from_database(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=strings.settings['all_operations_deleted'],
                         reply_markup=settings_kb)