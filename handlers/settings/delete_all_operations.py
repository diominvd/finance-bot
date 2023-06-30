from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data import database
import handlers
from keyboards import settings_kb
import lines
from states import SettingsStates

router = Router(name=__name__)

@router.message(SettingsStates.get_option, Text('Очистить список операций'))
async def settings_command_handler(message: Message, state: FSMContext):
    # Fetch all user operations from database.
    operations_list: list = database.select_operations_from_database_operations(user_id=handlers.fetch_user_id(obj=message))

    if len(operations_list) == 0:
        await message.answer(text=lines.settings_lines['error_text_operations_list_empty'],
                             reply_markup=settings_kb)
    else:
        # Delete all operations from database.
        database.delete_all_user_operations_from_database(user_id=handlers.fetch_user_id(obj=message))

        await message.answer(text=lines.settings_lines['text_all_operations_deleted'],
                             reply_markup=settings_kb)

    # Clear all states.
    await state.clear()